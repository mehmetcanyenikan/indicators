import pandas as pd
import numpy as np


class RSI:
    def __init__(self, df, period) -> None:
        self._df = df
        self._period = period

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    @property
    def period(self) -> int:
        return self._period

    @property
    def diffe(self) -> pd.DataFrame:
        return self._df['close'].diff()

    @property
    def wher_positive(self) -> pd.DataFrame:
        return np.where(self.diffe > 0, self.diffe, 0)

    @property
    def wher_negative(self) -> pd.DataFrame:
        return np.where(self.diffe < 0, -self.diffe, 0)

    @property
    def RS(self) -> pd.DataFrame:
        return np.mean(self.wher_positive[:self.period]) / np.mean(self.wher_negative[:self.period])

    @property
    def I(self) -> pd.DataFrame:
        return 100 - (100 / (1 + self.RS))
