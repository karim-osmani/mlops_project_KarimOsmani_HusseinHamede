from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


class TextNumericTransformer:
    def __init__(self, text_column, numeric_columns):
        self.text_column = text_column
        self.numeric_columns = numeric_columns
        self.text_vectorizer = TfidfVectorizer(max_features=5000)
        self.preprocessor = ColumnTransformer(
            transformers=[
                ("text", self.text_vectorizer, self.text_column),
                ("num", StandardScaler(), self.numeric_columns),
            ]
        )

    def transform(self, data, target=None):
        # Handle missing values for the text column
        data[self.text_column] = data[self.text_column].fillna("")

        # Prepare the data for transformation
        X = data[[self.text_column] + self.numeric_columns]
        y = data[target] if target else None

        # Apply transformation
        X_transformed = self.preprocessor.fit_transform(X)
        return X_transformed, y
