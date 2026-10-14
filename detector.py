import pandas as pd
from sklearn.ensemble import IsolationForest

from config import FEATURES, CONTAMINATION


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    model = IsolationForest(contamination=CONTAMINATION, random_state=42)
    df["anomaly"] = model.fit_predict(df[FEATURES]) == -1
    return df
