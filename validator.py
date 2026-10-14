import pandas as pd

from config import FEATURES


def validate(df: pd.DataFrame) -> pd.DataFrame:
    missing = {"time", *FEATURES} - set(df.columns)
    if missing:
        raise ValueError(f"Eksik kolonlar: {missing}")
    df = df.copy()
    df["time"] = pd.to_datetime(df["time"])
    df = df.dropna()
    if df.empty:
        raise ValueError("Veri boş")
    return df
