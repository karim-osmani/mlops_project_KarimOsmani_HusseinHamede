from sklearn.ensemble import RandomForestClassifier
from .base_model import Model


class RandomForestModel(Model):
    """A Random Forest model wrapper implementing the base Model interface."""

    def __init__(self, **kwargs):
        """Initialize the Random Forest model with the specified parameters.

        Args:
            **kwargs: Arbitrary keyword arguments passed to the RandomForestClassifier.
        """
        self.model = RandomForestClassifier(**kwargs)

    def train(self, X, y):
        """Train the Random Forest model on the provided data.

        Args:
            X: Features for training.
            y: Target labels.
        """
        self.model.fit(X, y)

    def predict(self, X):
        """Make predictions using the trained Random Forest model.

        Args:
            X: Features for prediction.

        Returns:
            Predictions for the input data.
        """
        return self.model.predict(X)
