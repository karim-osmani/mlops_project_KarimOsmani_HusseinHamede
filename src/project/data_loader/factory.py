from .dataframe_loader import DataFrameLoader
from .base_loader import DataLoader


class DataLoaderFactory:
    @staticmethod
    def get_data_loader(data_type: str, data: any) -> DataLoader:
        if data_type == "dataframe":
            return DataFrameLoader(data)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")
