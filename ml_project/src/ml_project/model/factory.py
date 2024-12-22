from .random_forest_model import RandomForestModel


class ModelFactory:
    @staticmethod
    def get_model(model_type: str, **kwargs) -> RandomForestModel:
        if model_type == "random_forest":
            return RandomForestModel(**kwargs)
        else:
            raise ValueError(f"Unsupported model type: {model_type}")
