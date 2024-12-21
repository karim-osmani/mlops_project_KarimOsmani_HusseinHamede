from .text_numeric_transformer import TextNumericTransformer


class TransformerFactory:
    @staticmethod
    def get_transformer(transform_type: str, **kwargs) -> TextNumericTransformer:
        if transform_type == "text_numeric":
            return TextNumericTransformer(
                kwargs["text_column"], kwargs["numeric_columns"]
            )
        else:
            raise ValueError(f"Unsupported transform type: {transform_type}")
