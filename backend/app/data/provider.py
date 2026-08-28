from abc import ABC, abstractmethod
from datetime import datetime

from app.data.models import Candle


class MarketDataProvider(ABC):

    @abstractmethod
    def get_candles(
        self,
        symbol: str,
        timeframe: str,
        start: datetime,
        end: datetime,
    ) -> list[Candle]:
        pass