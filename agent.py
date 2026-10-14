import time

import config
import storage
from detector import detect_anomalies
from fetcher import fetch_weather
from reporter import build_report, llm_summary
from states import Context, State
from validator import validate


class WeatherAgent:
    def __init__(self):
        self.ctx = Context()
        self.state = State.FETCH
        self.handlers = {
            State.FETCH: self._fetch,
            State.VALIDATE: self._validate,
            State.STORE: self._store,
            State.DETECT: self._detect,
            State.REPORT: self._report,
        }

    # --- durum işleyicileri: ince katman, işi modüllere devreder ---
    def _fetch(self) -> State:
        self.ctx.df = fetch_weather()
        return State.VALIDATE

    def _validate(self) -> State:
        self.ctx.df = validate(self.ctx.df)
        return State.STORE

    def _store(self) -> State:
        storage.save(self.ctx.df, config.RAW_PATH)
        return State.DETECT

    def _detect(self) -> State:
        df = storage.load(config.RAW_PATH)
        self.ctx.df = detect_anomalies(df)
        return State.REPORT

    def _report(self) -> State:
        storage.save(self.ctx.df, config.LABELED_PATH)
        print(llm_summary(build_report(self.ctx.df)))
        return State.DONE

    # --- FSM döngüsü ---
    def run(self) -> None:
        while self.state not in (State.DONE, State.ERROR):
            print(f"[state] {self.state.name}")
            try:
                self.state = self.handlers[self.state]()
            except Exception as e:
                if self.state == State.FETCH and self.ctx.retries < config.MAX_RETRIES:
                    self.ctx.retries += 1
                    print(f"[retry {self.ctx.retries}/{config.MAX_RETRIES}] {e}")
                    time.sleep(config.RETRY_WAIT_SEC)
                    continue
                self.ctx.error, self.state = e, State.ERROR
        if self.state == State.ERROR:
            print(f"Hata: {self.ctx.error}")
        else:
            print("Bitti")
