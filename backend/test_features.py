from datetime import datetime

from app.data.idx_provider import IDXProvider
from app.features.calculator import FeatureCalculator


provider = IDXProvider()

candles = provider.get_candles(
    symbol="BBRI",
    timeframe="1d",
    start=datetime(2026, 8, 1),
    end=datetime(2026, 8, 25),
)

calculator = FeatureCalculator()

df = calculator.calculate(candles)

print(df)