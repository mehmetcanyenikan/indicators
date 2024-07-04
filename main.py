import pandas as pd
import numpy as np


class data_read:
    def __init__(self, file_path: str, file_name: str) -> None:
        self._file_path = file_path
        self._file_name = file_name
        
    @property
    def file_path(self) -> str:
        return self._file_path
    
    @file_path.setter
    def file_path(self, value: str) -> None:
        self._file_path = value
        
    @property
    def file_name(self) -> str:
        return self._file_name
    
    @file_name.setter
    def file_name(self, value: str) -> None:
        self._file_path = value
    
    @property
    def data_read_csv(self) -> pd.DataFrame:
        df = pd.read_csv(self.file_path+self.file_name)
        return df
    
    
    
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
        return np.where(self.diffe > 0, self.diffe,0)
    
    @property
    def wher_negative(self) -> pd.DataFrame:
        return np.where(self.diffe < 0, -self.diffe,0)
    
    @property
    def RS(self) -> pd.DataFrame:
        return np.mean(self.wher_positive[:self.period]) / np.mean(self.wher_negative[:self.period])
    
    @property
    def I(self) -> pd.DataFrame:
        return 100 - (100 / (1 + self.RS))
    
        
def main():
    name = 'BTCUSDT-1m-2024-06-07.csv'
    path = '/home/can/Desktop/Indicators/'
    
    l1 = data_read(path, name)
    l2 = RSI(l1.data_read_csv, 10)
    print(l2.I)
    
    
    
if __name__ =='__main__':
    main()