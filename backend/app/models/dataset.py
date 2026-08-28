import pandas as pd

from app.models.label import Signal


class DatasetBuilder:

    def __init__(
        self,
        buy_threshold: float = 0.02,
        sell_threshold: float = -0.02,
    ):
        self.buy_threshold = buy_threshold
        self.sell_threshold = sell_threshold

    def build(self, df: pd.DataFrame) -> pd.DataFrame:

        data = df.copy()

        # Harga penutupan candle berikutnya
        data["future_close_1d"] = data["close"].shift(-1)

        # Return masa depan
        data["future_return_1d"] = (
            data["future_close_1d"] / data["close"]
        ) - 1

        # Label
        data["target"] = Signal.HOLD

        data.loc[
            data["future_return_1d"] >= self.buy_threshold,
            "target",
        ] = Signal.BUY

        data.loc[
            data["future_return_1d"] <= self.sell_threshold,
            "target",
        ] = Signal.SELL

        return data