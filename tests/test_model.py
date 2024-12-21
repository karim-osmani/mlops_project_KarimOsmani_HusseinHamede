# tests/test_model.py
import pandas as pd
import pytest
from project.model import RandomForestModel

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "feature1": [10.5, 15.2, 12.8],
        "feature2": [20.1, 25.3, 22.6],
        "target": [1, 0, 1]
    })

def test_random_forest_model(sample_data):
    X = sample_data[["feature1", "feature2"]]
    y = sample_data["target"]

    model = RandomForestModel(n_estimators=10, random_state=42)
    model.train(X, y)

    predictions = model.predict(X)

    assert predictions.shape[0] == X.shape[0]  # Ensure predictions match the number of samples
    assert all(pred in [0, 1] for pred in predictions)  # Ensure predictions are valid classes
