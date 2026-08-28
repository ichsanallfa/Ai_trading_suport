import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "AI IDX Scalper"
    VERSION = "0.1.0"
    ENVIRONMENT = "development"

    DEFAULT_TIMEFRAME = "1m"

    PREDICTION_HORIZONS = [
        "15m",
        "30m",
        "1h",
        "2h",
        "1d"
    ]

    CONFIDENCE_THRESHOLD = 0.70

    ZAPI_API_KEY = os.getenv("ZAPI_API_KEY")


settings = Settings()