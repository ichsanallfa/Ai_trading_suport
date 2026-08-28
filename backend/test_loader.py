from datetime import datetime

from app.data.loader import MarketDataLoader


loader = MarketDataLoader()

candles = loader.load(
    symbol="BBRI",
    start=datetime(2026, 8, 1),
    end=datetime(2026, 8, 25),
)

print(f"Jumlah candle: {len(candles)}")

for candle in candles[:3]:
    print(candle)