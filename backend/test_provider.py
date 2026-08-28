from datetime import datetime

from app.data.idx_provider import IDXProvider


provider = IDXProvider()

candles = provider.get_candles(
    symbol="BBRI",
    timeframe="1d",
    start=datetime(2026, 8, 1),
    end=datetime(2026, 8, 25),
)

print(f"Jumlah candle: {len(candles)}")

for candle in candles[:5]:
    print(candle)