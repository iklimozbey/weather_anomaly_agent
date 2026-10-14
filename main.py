from agents.weather_agent import WeatherAgent
from agents.crypto_agent import CryptoPriceAgent

def main():
    print("=== INITIALIZING MULTI-AGENT PROCESSED ENGINE ===\n")
    
    # 1. Hava Durumu Ajanını Çalıştırır
    weather_node = WeatherAgent()
    weather_node.execute_pipeline(output_path="data/weather_data.parquet")
    
    # 2. Kripto Para Ajanını Çalıştırır
    crypto_node = CryptoPriceAgent()
    crypto_node.execute_pipeline(output_path="data/crypto_data.parquet")
    
    print("All tasks processed by active agents have been shut down cleanly.")

if __name__ == "__main__":
    main()
