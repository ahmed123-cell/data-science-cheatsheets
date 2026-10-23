# Machine Learning

A collection of notebooks, notes, and projects covering core machine learning concepts — from building and evaluating models with scikit-learn to explaining model predictions using SHAP.

## 📖 Overview

This folder focuses on the practical side of machine learning: training models, understanding their properties, and interpreting their predictions. It's organized into two main areas — **Models** (building and applying ML models) and **SHAP** (explaining how those models make decisions).

## 📂 Contents

| Folder / File | Overview |
|---|---|
| `Models/` | ML model building and application — notebooks, explanations, and supporting images. |
| `Models/images/` | Images/diagrams used to support the explanations in the notebook and notes. |
| `Models/ML application notebook.ipynb` | Hands-on notebook applying machine learning models to a dataset. |
| `Models/models explaination.md` | Notes explaining the models used, how they work, and key concepts behind them. |
| `SHAP/` | Model interpretability — using SHAP (SHapley Additive exPlanations) to explain model predictions. |
| `SHAP/Data/` | Dataset(s) used in the SHAP notebook. |
| `SHAP/README.md` | Overview specific to the SHAP subfolder. |
| `SHAP/shap.ipynb` | Hands-on notebook demonstrating how to use SHAP to interpret and explain model outputs. |
| `scikit_learn properties.md` | Notes on scikit-learn's key properties, methods, and general usage patterns. |

## 🧠 What You'll Find

- **Model Building** — training, applying, and evaluating machine learning models using scikit-learn.
- **Model Interpretability (SHAP)** — understanding *why* a model makes a certain prediction, using feature importance and SHAP values.
- Supporting notes and diagrams to reinforce the concepts covered in each notebook.

## ▶️ How to Run

1. **Install the required libraries**:
   ```bash
   pip install scikit-learn shap pandas numpy matplotlib jupyter
   ```

2. **Launch Jupyter Notebook** from this folder:
   ```bash
   jupyter notebook
   ```

3. Open `Models/ML application notebook.ipynb` to explore model building, or `SHAP/shap.ipynb` to explore model explainability.

## 📚 Resources

- [Machine Learning Tutorial — GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/machine-learning/)

---
*This README will be updated as more models, notebooks, and notes are added to the folder.*