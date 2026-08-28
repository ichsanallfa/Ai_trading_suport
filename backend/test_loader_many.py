from datetime import datetime

from app.data.loader import MarketDataLoader
from app.data.universe import IDX_LIQUID_SYMBOLS


loader = MarketDataLoader()

data = loader.load_many(
    symbols=IDX_LIQUID_SYMBOLS,
    start=datetime(2026, 8, 1),
    end=datetime(2026, 8, 25),
)

for symbol, candles in data.items():
    print(f"{symbol}: {len(candles)} candle")