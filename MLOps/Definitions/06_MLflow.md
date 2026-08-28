Here’s the full content of the MLflow README:

---

# MLflow

**MLflow** is an open-source platform for managing the end-to-end machine learning lifecycle. It helps teams track experiments, package code for reproducibility, manage and deploy models, and collaboratively govern models in production.

> MLflow is library-agnostic — it works with any ML framework, language, or deployment tool.

---

## Overview

### What is MLflow?

MLflow provides a unified set of tools to organize, track, and operationalize machine learning and AI workflows. Originally focused on traditional ML, it has expanded to support LLMs, agents, and generative AI applications.

It is designed to be:

- **Open** – Works with any library, algorithm, or language
- **Lightweight** – Minimal changes needed to existing code
- **Extensible** – Supports plugins and custom integrations
- **Production-ready** – Covers the full path from experimentation to deployment

### Core Components

| Component              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **MLflow Tracking**    | Log parameters, metrics, code versions, and artifacts. Includes a powerful UI for comparing runs. |
| **MLflow Models**      | Standard format for packaging models from any library for easy deployment (batch, real-time, Docker, cloud). |
| **MLflow Model Registry** | Centralized model store with versioning, stage transitions (Staging → Production), and annotations. |
| **MLflow Projects**    | Standard format for packaging reusable, reproducible data science code.     |
| **MLflow Recipes**     | Predefined templates for common tasks (classification, regression, etc.).   |

> Recent versions also include strong support for **LLM tracing, evaluation, prompt management, and AI Gateway**.

### Key Benefits

| Benefit                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Experiment Tracking      | Easily record and compare hyperparameters, metrics, and artifacts           |
| Reproducibility          | Package code, environment, and models so anyone can re-run experiments      |
| Model Management         | Version, stage, and deploy models from a central registry                   |
| Framework Agnostic       | Works with scikit-learn, PyTorch, TensorFlow, XGBoost, Hugging Face, etc.   |
| Deployment Flexibility   | Serve models locally, via Docker, Spark, SageMaker, Azure ML, and more      |
| Collaboration            | Share results via Tracking Server or Databricks                             |
| LLM & Agent Support      | Tracing, evaluation, prompt versioning, and observability for GenAI         |

---

## Installation

```bash
# Basic installation
pip install mlflow

# With extras (optional)
pip install mlflow[extras]
```

Verify installation:

```bash
mlflow --version
```

---

## Popular Commands

### 1. Tracking Server & UI

| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `mlflow ui`              | Start the local Tracking UI (default: http://localhost:5000) |
| `mlflow server`          | Start a full Tracking Server (supports remote clients) |
| `mlflow doctor`          | Diagnose installation and environment issues     |

```bash
# Simple local UI
mlflow ui

# Production-style server with SQLite backend
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns \
  --host 0.0.0.0 \
  --port 5000
```

### 2. Experiments

| Command                              | Description                          |
|--------------------------------------|--------------------------------------|
| `mlflow experiments create -n <name>`| Create a new experiment              |
| `mlflow experiments search`          | List / search experiments            |
| `mlflow experiments delete -x <id>`  | Delete an experiment                 |
| `mlflow experiments rename`          | Rename an experiment                 |

### 3. Runs

| Command                          | Description                              |
|----------------------------------|------------------------------------------|
| `mlflow runs list`               | List runs in an experiment               |
| `mlflow runs describe --run-id`  | Show details of a specific run           |
| `mlflow runs delete --run-id`    | Delete a run                             |

### 4. Projects

| Command                    | Description                                      |
|----------------------------|--------------------------------------------------|
| `mlflow run <uri>`         | Run an MLflow Project (local path or Git URL)    |
| `mlflow run . -P param=value` | Run current project with parameters           |

```bash
# Run a project from GitHub
mlflow run https://github.com/mlflow/mlflow-example

# Run local project with parameters
mlflow run . -P alpha=0.5 -P l1_ratio=0.1
```

### 5. Models

| Command                              | Description                                      |
|--------------------------------------|--------------------------------------------------|
| `mlflow models serve -m <model_uri>` | Serve a model as a local REST API                |
| `mlflow models predict -m <uri> -i <file>` | Run batch predictions on a CSV/JSON file    |
| `mlflow models build-docker -m <uri>`| Build a Docker image for the model               |

```bash
# Serve a model from a run
mlflow models serve -m runs:/<run_id>/model -p 5001

# Serve a registered model
mlflow models serve -m models:/MyModel/Production -p 5001
```

### 6. Artifacts

| Command                              | Description                          |
|--------------------------------------|--------------------------------------|
| `mlflow artifacts list --run-id`     | List artifacts of a run              |
| `mlflow artifacts download --run-id` | Download artifacts                   |
| `mlflow artifacts log-artifacts`     | Log a directory of artifacts         |

### 7. Other Useful Commands

| Command                  | Description                                      |
|--------------------------|--------------------------------------------------|
| `mlflow gc`              | Garbage-collect deleted runs and artifacts       |
| `mlflow deployments`     | Manage model deployments to various targets      |
| `mlflow traces ...`      | Manage LLM/agent traces (search, get, evaluate)  |

---

## Typical Workflow

```bash
# 1. Install & start UI
pip install mlflow
mlflow ui

# 2. In your Python code
import mlflow

mlflow.set_experiment("my-experiment")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.sklearn.log_model(model, "model")

# 3. Compare runs in the UI at http://localhost:5000

# 4. Register the best model
# (via UI or API)

# 5. Serve the model
mlflow models serve -m models:/MyModel/1 -p 5001
```

### Python Tracking API (most common usage)

```python
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("classification")

with mlflow.start_run(run_name="rf-trial"):
    mlflow.log_params({"n_estimators": 100, "max_depth": 5})
    mlflow.log_metric("f1", 0.87)
    mlflow.sklearn.log_model(model, "model")
    mlflow.log_artifact("confusion_matrix.png")
```

---

## Resources

- **Official Docs**: [https://mlflow.org/docs/latest/](https://mlflow.org/docs/latest/)
- **Website**: [https://mlflow.org](https://mlflow.org)
- **GitHub**: [https://github.com/mlflow/mlflow](https://github.com/mlflow/mlflow)
- **CLI Reference**: [https://mlflow.org/docs/latest/cli.html](https://mlflow.org/docs/latest/cli.html)
- **Quickstart**: [https://mlflow.org/docs/latest/quickstart.html](https://mlflow.org/docs/latest/quickstart.html)

---

## License

MLflow is released under the **Apache 2.0** license.

---

You can also find the file at: `/home/workdir/artifacts/README-MLflow.md`