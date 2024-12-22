import pandas as pd
from .base_loader import DataLoader


class DataFrameLoader(DataLoader):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def load_data(self) -> pd.DataFrame:
        return self.df
