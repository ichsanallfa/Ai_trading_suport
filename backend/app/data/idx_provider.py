from datetime import datetime

import requests

from app.core.config import settings
from app.data.models import Candle
from app.data.provider import MarketDataProvider


class IDXProvider(MarketDataProvider):

    BASE_URL = "https://api.zpi.web.id/v1/finance:idx"

    def get_candles(
        self,
        symbol: str,
        timeframe: str,
        start: datetime,
        end: datetime,
    ) -> list[Candle]:

        if timeframe != "1d":
            raise ValueError(
                "IDXProvider saat ini menggunakan data harian (1d)."
            )

        url = f"{self.BASE_URL}/stock-history"

        params = {
            "code": symbol,
            "from": start.strftime("%Y-%m-%d"),
            "to": end.strftime("%Y-%m-%d"),
        }

        headers = {
            "x-api-key": settings.ZAPI_API_KEY
        }

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=30,
        )

        response.raise_for_status()

        result = response.json()

        candles = []

        items = result.get("data", {}).get("items", [])

        for item in items:
            candle = Candle(
                timestamp=datetime.fromisoformat(item["date"]),
                open=float(item["open"]),
                high=float(item["high"]),
                low=float(item["low"]),
                close=float(item["close"]),
                volume=int(item["volume"]),
            )

            candles.append(candle)

        return candles