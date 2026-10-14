from pathlib import Path

DATA_DIR = Path("data")
RAW_PATH = DATA_DIR / "weather.parquet"
LABELED_PATH = DATA_DIR / "weather_labeled.parquet"

API_URL = "https://api.open-meteo.com/v1/forecast"
API_PARAMS = {
    "latitude": 39.93,   # Ankara
    "longitude": 32.86,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    "past_days": 14,
    "forecast_days": 1,
}

FEATURES = ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"]
CONTAMINATION = 0.02
MAX_RETRIES = 3
RETRY_WAIT_SEC = 2
