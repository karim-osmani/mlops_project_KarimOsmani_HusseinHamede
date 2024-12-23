import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from project.config import load_config
from project.data_loader.factory import DataLoaderFactory
from project.data_transform.factory import TransformerFactory
from project.model.factory import ModelFactory

def main():
    # Load configuration
    config = load_config("D:/AData science/USJ/S3/software/project/config/config.yaml")
    print("Loaded Config:", config)
    mlflow.set_tracking_uri("file:/D:/AData science/USJ/S3/software/project/mlruns")

    # Set MLflow experiment
    mlflow.set_experiment("ML Data Pipeline Experiment")

    # Start an MLflow run
    with mlflow.start_run():
        # Log configuration parameters
        mlflow.log_param("file_type", config.data_loader.file_type)
        mlflow.log_param("normalize", config.transformation.normalize)
        mlflow.log_param("scaling_method", config.transformation.scaling_method)

        # Load data
        if config.data_loader.file_type == "csv":
            df = pd.read_csv(config.data_loader.file_path)
        elif config.data_loader.file_type == "json":
            df = pd.read_json(config.data_loader.file_path)
        else:
            raise ValueError(f"Unsupported file type: {config.data_loader.file_type}")

        # Check if text_column exists in the dataframe
        if config.text_column not in df.columns:
            raise ValueError(f"{config.text_column} is not found in the data columns.")
        df[config.text_column] = df[config.text_column].fillna("")

        # Transform data
        transformer = TransformerFactory.get_transformer(
            "text_numeric",
            text_column=config.text_column,
            numeric_columns=config.numeric_columns,
        )
        X, y = transformer.transform(df, target=config.target_column)

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Train model
        model = ModelFactory.get_model("random_forest", random_state=42)
        model.train(X_train, y_train)

        # Log the model to MLflow
        mlflow.sklearn.log_model(model.model, "random_forest_model")

        # Predict
        y_pred = model.predict(X_test)

        # Evaluate
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)

        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        for label, metrics in report.items():
            if isinstance(metrics, dict):
                for metric_name, metric_value in metrics.items():
                    mlflow.log_metric(f"{label}_{metric_name}", metric_value)

        # Print evaluation results
        print("Accuracy:", accuracy)
        print("Classification Report:", classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()
