from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

import pandas as pd


class State(Enum):
    FETCH = auto()
    VALIDATE = auto()
    STORE = auto()
    DETECT = auto()
    REPORT = auto()
    DONE = auto()
    ERROR = auto()


@dataclass
class Context:
    """Durumlar arasında taşınan ortak veri."""
    df: Optional[pd.DataFrame] = None
    error: Optional[Exception] = None
    retries: int = 0
