import pandas as pd
import numpy as np


class change:
    def __init__(self, df) -> None:
        self._df = df

    @property
    def diffe(self) -> pd.DataFrame:
        return self._df['close'].diff()


class gain(change):
    def __init__(self, df) -> None:
        super().__init__(df)

    @property
    def wher_positive(self) -> pd.DataFrame:
        return pd.DataFrame(np.where(self.diffe.isna(), self.diffe, np.where(self.diffe > 0, self.diffe, 0)))


class loss(change):
    def __init__(self, df) -> None:
        super().__init__(df)

    @property
    def wher_negative(self) -> pd.DataFrame:
        return pd.DataFrame(np.where(self.diffe.isna(),self.diffe, np.where(self.diffe < 0, -self.diffe,0)))


class avg_gain(gain):
    def __init__(self, df, period) -> None:
        super().__init__(df)
        self._period = period

    @property
    def avg_gain_positive(self):
        avg_gain_prev = self.wher_positive[0].rolling(window=self._period).mean()
        current_gain = self.wher_positive[0]
        for i in range(self._period, len(self.wher_positive)-1):
            avg_gain_prev[i+1] = ((avg_gain_prev[i] * 13) + current_gain[i+1])/self._period
        return avg_gain_prev


class avg_loss(loss):
    def __init__(self, df, period) -> None:
        super().__init__(df)
        self._period = period

    @property
    def avg_gain_negative(self):
        avg_gain_prev = self.wher_negative[0].rolling(window=self._period).mean()
        current_gain = self.wher_negative[0]
        for i in range(self._period, len(self.wher_negative)-1):
            avg_gain_prev[i+1] = ((avg_gain_prev[i] * 13) + current_gain[i+1])/self._period
        return avg_gain_prev


class RSI():
    def __init__(self, avg_gain_positive, avg_gain_negative) -> None:
        self.avg_gain_positive = avg_gain_positive
        self.avg_gain_negative = avg_gain_negative

    @property
    def RS(self) -> pd.DataFrame:
        return self.avg_gain_positive / self.avg_gain_negative

    @property
    def RSi(self) -> pd.DataFrame:
        return 100 - (100 / (1 + self.RS))
