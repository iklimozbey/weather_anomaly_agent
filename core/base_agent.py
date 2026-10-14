from abc import ABC, abstractmethod
import pandas as pd

class BaseAgent(ABC):
    """
    Abstract base class defining the standard data pipeline structure.
    """
    def __init__(self, agent_name: str):
        self.agent_name = agent_name

    @abstractmethod
    def fetch_data(self) -> pd.DataFrame:
        """Fetch raw data from source."""
        pass

    @abstractmethod
    def validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Validate and clean the fetched data."""
        pass

    @abstractmethod
    def detect_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply statistical algorithms to find anomalies."""
        pass

    def execute_pipeline(self, output_path: str):
        """Standardized lifecycle: FETCH -> VALIDATE -> DETECT -> STORE"""
        print(f"{self.agent_name} pipeline lifecycle started.")
        
        # 1. FETCH
        print("[STATUS] FETCH")
        raw_df = self.fetch_data()
        
        # 2. VALIDATE
        print("[STATUS] VALIDATE")
        clean_df = self.validate_data(raw_df)
        
        # 3. DETECT
        print("[STATUS] DETECT")
        processed_df = self.detect_anomalies(clean_df)
        
        # 4. STORE
        print("[STATUS] STORE")
        processed_df.to_parquet(output_path)
        
        print(f"{self.agent_name} pipeline successfully completed.\n")
