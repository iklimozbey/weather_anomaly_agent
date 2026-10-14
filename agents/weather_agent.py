import pandas as pd
import numpy as np
import random
from core.base_agent import BaseAgent

class WeatherAgent(BaseAgent):
    def __init__(self):
        super().__init__(agent_name="[Weather Agent]")

    def fetch_data(self) -> pd.DataFrame:
        timestamps = pd.date_range(start="2026-01-01", periods=100, freq="D")
        
        # Temel sıcaklık simülasyonu
        np.random.seed(42)
        temperatures = [float(20 + random.uniform(-5, 5)) for _ in range(100)]
        
        # Yapay anomaliler ekleyelim (Belirli günlere şok sıcaklık)
        temperatures[15] = 45.2
        temperatures[42] = 42.7
        temperatures[78] = 41.0
        
        df = pd.DataFrame({
            "timestamp": timestamps,
            "temperature": temperatures
        })
        
        # DETAYLI LOG
        print(f"   [INFO] Successfully simulated {len(df)} days of weather records.")
        print(f"   [INFO] Date Range: {df['timestamp'].min().strftime('%Y-%m-%d')} to {df['timestamp'].max().strftime('%Y-%m-%d')}")
        return df

    def validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        initial_count = len(df)
        df = df.dropna()
        print(f"   [INFO] Data Validation Status: Clean. Rows passed: {len(df)}/{initial_count}")
        return df

    def detect_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        # 40 derecenin üzeri anomali
        df["is_anomaly"] = df["temperature"] > 40
        
        # İstatistikleri hesapla
        avg_temp = df["temperature"].mean()
        max_temp = df["temperature"].max()
        anomalies = df[df["is_anomaly"] == True]
        
        # DETAYLI ÇIKTI PANELİ
        print("   " + "="*50)
        print("   📊 WEATHER ANOMALY DETECTION REPORT")
        print("   " + "="*50)
        print(f"   • Overall Average Temp : {avg_temp:.2f}°C")
        print(f"   • Maximum Recorded Temp: {max_temp:.2f}°C")
        print(f"   • Total Anomalies Found: {len(anomalies)} critical events")
        print("\n   🚨 Detected Anomaly Logs:")
        for idx, row in anomalies.iterrows():
            print(f"     -> [CRITICAL] Date: {row['timestamp'].strftime('%Y-%m-%d')} | Temp: {row['temperature']:.1f}°C (Threshold > 40°C)")
        print("   " + "="*50)
        
        return df
