# Data Version Control (DVC)

**DVC** is a free, open-source tool for data management, ML pipeline automation, and experiment tracking. It brings software engineering best practices to data science and machine learning by enabling version control for large datasets, models, and experiments — much like Git does for code.

> **Think of DVC as “Git for data.”**

---

## Overview

### What is DVC?

DVC (Data Version Control) helps data science and ML teams:

- **Version large datasets and models** without storing them in Git
- **Reproduce experiments** reliably
- **Build and automate ML pipelines**
- **Collaborate** securely using familiar tools (Git, cloud storage, CI/CD)

It works on top of Git repositories and external storage (local, S3, GCS, Azure, SSH, etc.). Lightweight metadata files (`.dvc` and `dvc.yaml`) are committed to Git, while the actual data lives in a local cache or remote storage.

### Core Principles

1. **Codification** – Describe data, models, pipelines, and experiments in human-readable metafiles.
2. **Versioning** – Use Git to version the entire ML project (code + data pointers).
3. **Secure collaboration** – Share projects while controlling access to large data assets.

### Key Benefits

| Benefit              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Lightweight          | No servers or databases required                                            |
| Git-compatible       | Works seamlessly with existing Git workflows                                |
| Reproducible         | Easily restore previous data/model versions and re-run pipelines            |
| Efficient            | Content-addressable storage avoids duplication; only changed data is stored |
| Cloud-agnostic       | Supports many remote storage backends                                       |
| Experiment tracking  | Track metrics, parameters, and plots alongside code                         |

### How DVC Works

1. **Git for Metadata** – Stores `.dvc` files and `dvc.yaml` that point to data versions.
2. **Local Cache** – Actual data is stored in `.dvc/cache` using content-addressable hashing.
3. **Remote Storage** – Data can be pushed/pulled to/from cloud or on-prem storage.

---

## Installation

```bash
# Recommended (modern)
uv tool install dvc
# or
pipx install dvc

# Alternative
pip install dvc
```

Verify installation:

```bash
dvc --help
dvc version
```

> **Note:** Git must be installed. DVC does not replace Git.

---

## Popular Commands

### 1. Project Setup

| Command          | Description                                      |
|------------------|--------------------------------------------------|
| `dvc init`       | Initialize a DVC project inside a Git repository |
| `dvc destroy`    | Remove all DVC-related files and cache           |
| `dvc version`    | Show DVC version and environment information     |
| `dvc config`     | Get or set configuration options                 |

```bash
git init
dvc init
git commit -m "Initialize DVC"
```

### 2. Data Management

| Command            | Description                                              |
|--------------------|----------------------------------------------------------|
| `dvc add <path>`   | Track a file or directory with DVC                       |
| `dvc remove <path>`| Stop tracking a file/directory and remove its `.dvc` file|
| `dvc status`       | Show changes in tracked data and pipeline stages         |
| `dvc commit`       | Save changed data to the local cache                     |
| `dvc checkout`     | Restore data files from the cache                        |
| `dvc diff`         | Show differences in data between commits                 |

```bash
dvc add data/dataset.csv
git add data/dataset.csv.dvc data/.gitignore
git commit -m "Add dataset"
```

### 3. Remote Storage

| Command                      | Description                                      |
|------------------------------|--------------------------------------------------|
| `dvc remote add <name> <url>`| Add a remote storage location                    |
| `dvc remote list`            | List configured remotes                          |
| `dvc remote modify`          | Modify remote settings                           |
| `dvc push`                   | Upload data to remote storage                    |
| `dvc pull`                   | Download data from remote storage                |
| `dvc fetch`                  | Download data to cache without linking to workspace |

```bash
dvc remote add -d myremote s3://mybucket/dvcstore
dvc push
dvc pull
```

### 4. Pipelines

| Command                    | Description                                                |
|----------------------------|------------------------------------------------------------|
| `dvc stage add`            | Define a pipeline stage                                    |
| `dvc repro`                | Reproduce the pipeline (runs only changed stages)          |
| `dvc dag`                  | Visualize the pipeline as a directed graph                 |
| `dvc params`               | Show or manage parameters                                  |
| `dvc metrics show`         | Display metrics                                            |
| `dvc metrics diff`         | Compare metrics between commits/experiments                |
| `dvc plots`                | Visualize and compare plots                                |

Example stage:

```bash
dvc stage add -n preprocess \
  -d data/raw.csv \
  -o data/processed.csv \
  python preprocess.py

dvc stage add -n train \
  -d data/processed.csv \
  -d src/train.py \
  -o models/model.pkl \
  -M metrics.json \
  python src/train.py
```

### 5. Experiments

| Command              | Description                                      |
|----------------------|--------------------------------------------------|
| `dvc exp run`        | Run an experiment                                |
| `dvc exp show`       | Show experiment results in a table               |
| `dvc exp diff`       | Compare experiments                              |
| `dvc exp apply`      | Apply an experiment’s results to the workspace   |
| `dvc exp push/pull`  | Share experiments via Git                        |

### 6. Utility & Maintenance

| Command          | Description                                          |
|------------------|------------------------------------------------------|
| `dvc gc`         | Garbage-collect unused data from cache               |
| `dvc cache`      | Manage cache settings                                |
| `dvc list` / `dvc ls` | List files in a DVC repository (local or remote) |
| `dvc get`        | Download a file/directory from any DVC repo          |
| `dvc import`     | Import and track data from another DVC/Git repo      |

---

## Typical Workflow

```bash
# 1. Initialize
git init && dvc init

# 2. Track data
dvc add data/
git add data/.dvc data/.gitignore
git commit -m "Track data"

# 3. Configure remote
dvc remote add -d storage s3://my-bucket/dvc
dvc push

# 4. Define & run pipeline
dvc stage add ...
dvc repro

# 5. Track metrics & experiments
dvc metrics show
dvc exp run ...

# 6. Share
git push
dvc push
```

---

## Resources

- **Official Docs**: [https://doc.dvc.org](https://doc.dvc.org)
- **GitHub**: [https://github.com/treeverse/dvc](https://github.com/treeverse/dvc)
- **Website**: [https://dvc.org](https://dvc.org)
- **Command Reference**: [https://doc.dvc.org/command-reference](https://doc.dvc.org/command-reference)

---

## License

DVC is released under the **Apache 2.0** license.
