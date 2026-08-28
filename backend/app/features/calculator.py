import pandas as pd

from app.data.models import Candle


class FeatureCalculator:

    def calculate(self, candles: list[Candle]) -> pd.DataFrame:
        data = [
            {
                "timestamp": candle.timestamp,
                "open": candle.open,
                "high": candle.high,
                "low": candle.low,
                "close": candle.close,
                "volume": candle.volume,
            }
            for candle in candles
        ]

        df = pd.DataFrame(data)

        if df.empty:
            return df

        # Pastikan data berdasarkan waktu lama → terbaru
        df = df.sort_values("timestamp").reset_index(drop=True)

        # =========================
        # PRICE
        # =========================

        df["return_1d"] = df["close"].pct_change()

        # Volatility 5 periode
        df["volatility_5"] = (
            df["return_1d"]
            .rolling(window=5)
            .std()
        )

        # =========================
        # TREND
        # =========================

        df["sma_5"] = (
            df["close"]
            .rolling(window=5)
            .mean()
        )

        df["sma_10"] = (
            df["close"]
            .rolling(window=10)
            .mean()
        )

        df["ema_5"] = (
            df["close"]
            .ewm(span=5, adjust=False)
            .mean()
        )

        # =========================
        # MOMENTUM
        # =========================

        delta = df["close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()

        rs = avg_gain / avg_loss

        df["rsi_14"] = 100 - (100 / (1 + rs))

        # =========================
        # VOLUME
        # =========================

        df["volume_change"] = df["volume"].pct_change()

        return df