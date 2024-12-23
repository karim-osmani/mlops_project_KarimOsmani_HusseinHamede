# ML Data Pipeline with Monitoring and MLflow

This project implements a machine learning pipeline for training, evaluating, and monitoring models. It includes integrated experiment tracking using MLflow and monitoring with Prometheus.

---

## **Table of Contents**
- [Features](#features)
- [Project Structure](#project-structure)
- [System Requirements](#system-requirements)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Running Inference](#running-inference)
  - [Accessing MLflow Dashboard](#accessing-mlflow-dashboard)
  - [Accessing Prometheus Metrics](#accessing-prometheus-metrics)
- [Monitoring and Metrics](#monitoring-and-metrics)
- [Contribution Guidelines](#contribution-guidelines)

---

## **Features**
- **Data Loading and Transformation**
  - Supports CSV and JSON file formats.
  - Text and numeric feature preprocessing.

- **Model Training and Evaluation**
  - Uses Random Forest classifier.
  - Tracks accuracy and detailed classification metrics.

- **Experiment Tracking with MLflow**
  - Tracks model parameters, metrics, and artifacts.

- **Monitoring with Prometheus**
  - Exposes custom metrics like request count, training duration, and model accuracy.

---



## **System Requirements**
- **Python Version**: 3.11
- **Dependencies**:
  - `mlflow`
  - `prometheus-client`
  - `pandas`
  - `scikit-learn`
- **Prometheus**:
  - [Download Prometheus](https://prometheus.io/download/)

---

## **Installation Instructions**
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/ml_data_pipeline.git
   cd ml_data_pipeline
   ```

2. **Set Up Python Environment**
   ```bash
   poetry install
   poetry shell
   ```

3. **Install Prometheus**
   - Download and extract Prometheus.
   - Move `prometheus.yml` and `alert.rules.yml` to the `prometheus/` directory.

4. **Run Prometheus**
   ```bash
   cd prometheus
   prometheus --config.file=prometheus.yml
   ```

---

## **Usage**

### **Training the Model**
Run the training pipeline:
```bash
poetry run train
```

### **Running Inference**
Perform inference using the trained model:
```bash
poetry run inference --word_count 10 --char_count 50 --sentiment 0.5 --any_neg 0
```

### **Accessing MLflow Dashboard**
1. Start MLflow Tracking Server:
   ```bash
   mlflow ui
   ```
2. Open the MLflow UI at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### **Accessing Prometheus Metrics**
1. Visit the Prometheus dashboard:
   ```
   http://localhost:9090
   ```
2. View metrics exposed by the pipeline:
   ```bash
   curl http://localhost:8000/metrics
   ```

---

## **Monitoring and Metrics**
- **Custom Metrics**
  - `requests_total`: Total number of requests to the pipeline.
  - `train_duration_seconds`: Time spent training the model.
  - `model_accuracy`: Accuracy of the trained model.

- **Prometheus Integration**
  - Metrics are exposed on the `/metrics` endpoint.

- **Alerting Rules**
  - Configure `alert.rules.yml` to define custom alerts (e.g., accuracy dropping below a threshold).

---

## **Contribution Guidelines**
1. **Fork the Repository**
   - Create a new branch for your feature/bugfix.

2. **Set Up Local Environment**
   - Follow the [Installation Instructions](#installation-instructions).

3. **Run Tests**
   - Add and validate tests in the `tests/` directory.
   ```bash
   pytest tests/
   ```

4. **Commit and Push**
   ```bash
   git add .
   git commit -m "Add your message here"
   git push origin <branch-name>
   ```

5. **Create a Pull Request**
   - Submit your changes for review.

---

## **Future Enhancements**
- Add Docker support for containerized deployment.
- Extend alerting capabilities with Grafana.
- Automate CI/CD pipeline integration.

---



