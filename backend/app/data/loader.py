from datetime import datetime

from app.data.idx_provider import IDXProvider
from app.data.models import Candle


class MarketDataLoader:

    def __init__(self):
        self.provider = IDXProvider()

    def load(
        self,
        symbol: str,
        start: datetime,
        end: datetime,
        timeframe: str = "1d",
    ) -> list[Candle]:

        return self.provider.get_candles(
            symbol=symbol,
            timeframe=timeframe,
            start=start,
            end=end,
        )

    def load_many(
        self,
        symbols: list[str],
        start: datetime,
        end: datetime,
        timeframe: str = "1d",
    ) -> dict[str, list[Candle]]:

        result = {}

        for symbol in symbols:
            result[symbol] = self.load(
                symbol=symbol,
                start=start,
                end=end,
                timeframe=timeframe,
            )

        return result