import pandas as pd


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
