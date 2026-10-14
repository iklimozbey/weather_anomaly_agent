from pathlib import Path

import pandas as pd


def save(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)


def load(path: Path) -> pd.DataFrame:
    return pd.read_parquet(path)
