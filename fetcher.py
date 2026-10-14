import pandas as pd
import requests

from config import API_URL, API_PARAMS


def fetch_weather() -> pd.DataFrame:
    r = requests.get(API_URL, params=API_PARAMS, timeout=10)
    r.raise_for_status()
    return pd.DataFrame(r.json()["hourly"])
