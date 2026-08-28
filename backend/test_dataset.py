from datetime import datetime
from app.data.idx_provider import IDXProvider
from app.features.calculator import FeatureCalculator
from app.models.dataset import DatasetBuilder


provider = IDXProvider()

candles = provider.get_candles(
    symbol="BBRI",
    timeframe="1d",
    start=datetime(2026, 8, 1),
    end=datetime(2026, 8, 25),
)

calculator = FeatureCalculator()

features = calculator.calculate(candles)

builder = DatasetBuilder()

dataset = builder.build(features)

print(
    dataset[
        [
            "timestamp",
            "close",
            "future_close_1d",
            "future_return_1d",
            "target",
        ]
    ]
)