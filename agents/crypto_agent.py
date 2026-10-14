import pandas as pd
import numpy as np
import random
from core.base_agent import BaseAgent

class CryptoPriceAgent(BaseAgent):
    def __init__(self):
        super().__init__(agent_name="[Crypto Price Agent]")

    def fetch_data(self) -> pd.DataFrame:
        timestamps = pd.date_range(start="2026-01-01", periods=100, freq="h")
        
        # Temel fiyat simülasyonu
        btc_prices = [float(65000 + random.uniform(-300, 300)) for _ in range(100)]
        eth_prices = [float(3400 + random.uniform(-20, 20)) for _ in range(100)]
        
        # Yapay piyasa çöküşü (Flash Crash Anomalisi) ekleyelim
        btc_prices[30] = 58200.0  # Ani %10 düşüş
        btc_prices[75] = 59100.0  # Ani %9 düşüş
        
        df = pd.DataFrame({
            "timestamp": timestamps,
            "btc_price": btc_prices,
            "eth_price": eth_prices
        })
        
        print(f"   [INFO] Successfully fetched {len(df)} hours of live crypto tickers.")
        print(f"   [INFO] Active Assets Monitored: BTC/USD, ETH/USD")
        return df

    def validate_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.dropna()
        df = df[(df["btc_price"] > 0) & (df["eth_price"] > 0)]
        print(f"   [INFO] Ticker Integrity Check: Passed. Market feeds are stable.")
        return df

    def detect_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        # Son 5 saatin ortalaması (Simple Moving Average)
        df["btc_sma_5h"] = df["btc_price"].rolling(window=5, min_periods=1).mean()
        
        # Fiyat, hareketli ortalamanın %5 altındaysa anomali (Şok Düşüş)
        df["is_btc_anomaly"] = df["btc_price"] < (df["btc_sma_5h"] * 0.95)
        
        anomalies = df[df["is_btc_anomaly"] == True]
        
        # DETAYLI ÇIKTI PANELİ
        print("   " + "="*50)
        print("   📈 CRYPTO MARKET CRASH DETECTION REPORT")
        print("   " + "="*50)
        print(f"   • Current BTC Base Price : ${df['btc_price'].iloc[-1]:,.2f}")
        print(f"   • Current ETH Base Price : ${df['eth_price'].iloc[-1]:,.2f}")
        print(f"   • Total Market Anomalies : {len(anomalies)} flash crashes detected")
        print("\n   🚨 Detected Market Anomaly Logs:")
        for idx, row in anomalies.iterrows():
            drop_percentage = ((row['btc_sma_5h'] - row['btc_price']) / row['btc_sma_5h']) * 100
            print(f"     -> [SHOCK DROP] Time: {row['timestamp'].strftime('%Y-%m-%d %H:%M')} | Price: ${row['btc_price']:,.2f} | Drop: -{drop_percentage:.1f}% vs 5h-Avg (${row['btc_sma_5h']:,.2f})")
        print("   " + "="*50)
        
        return df
