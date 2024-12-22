import argparse
import pandas as pd  # Ensure you import pandas
from ml_project.config import load_config  # Ensure this line is present
from ml_project.data_loader.factory import DataLoaderFactory
from ml_project.data_transform.factory import TransformerFactory
from ml_project.model.factory import ModelFactory


def main():
    # Load configuration
    config = load_config("config/config.yaml")

    # Print config to debug and check
    print("Loaded Config:", config)

    # Load data (replace ellipsis with actual data loading)
    if config.data_loader.file_type == "csv":
        df = pd.read_csv(config.data_loader.file_path)  # Reading the CSV file
    elif config.data_loader.file_type == "json":
        df = pd.read_json(config.data_loader.file_path)  # Reading the JSON file
    else:
        raise ValueError(f"Unsupported file type: {config.data_loader.file_type}")

    # Check if text_column exists in the dataframe
    if config.text_column not in df.columns:
        raise ValueError(f"{config.text_column} is not found in the data columns.")

    # Handle missing values in the text column
    df[config.text_column] = df[config.text_column].fillna("")

    # Transform data
    transformer = TransformerFactory.get_transformer(
        "text_numeric",
        text_column=config.text_column,
        numeric_columns=config.numeric_columns,
    )
    X, y = transformer.transform(df, target=config.target_column)

    # Split data
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = ModelFactory.get_model("random_forest", random_state=42)
    model.train(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Evaluate
    from sklearn.metrics import accuracy_score, classification_report

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:", classification_report(y_test, y_pred))


if __name__ == "__main__":
    main()
