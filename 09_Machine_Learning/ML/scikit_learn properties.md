# scikit-learn Properties & Key Modules 📦

## Handling Missing Values with `sklearn.impute`

Missing data is a common problem in real-world datasets. Scikit-learn provides powerful tools in the `sklearn.impute` module to handle missing values effectively.

---

### 1. SimpleImputer 🧼

**SimpleImputer** is a straightforward and fast method to replace missing values (NaN) with a constant or statistical value.

#### How It Works:
- It replaces missing values using a simple strategy calculated from the available data in each column.

#### Main Strategies:
- `"mean"` → Replaces with the **mean** of the column (best for numeric data)
- `"median"` → Replaces with the **median** of the column (robust to outliers)
- `"most_frequent"` → Replaces with the **mode** (best for categorical data)
- `"constant"` → Replaces with a fixed value (e.g., 0 or -1)

#### Example Usage:
```python
from sklearn.impute import SimpleImputer
import numpy as np

imputer = SimpleImputer(strategy='mean')        # or 'median', 'most_frequent'
imputer.fit(X_train)                            # Learn parameters from training data
X_train_imputed = imputer.transform(X_train)
X_test_imputed = imputer.transform(X_test)      # Use same parameters on test data
```

**Advantages** ✅:
- Very fast and simple
- Easy to interpret
- Works well as a baseline

**Disadvantages** ❌:
- Does not consider relationships between features
- Can distort data distribution if missingness is high

---

### 2. KNNImputer 🧑‍🤝‍🧑

**KNNImputer** uses the **K-Nearest Neighbors** algorithm to impute missing values by looking at similar samples.

#### How It Works:
1. For each missing value, it finds the **K nearest neighbors** (based on other features).
2. It takes the average (or weighted average) of those neighbors' values to fill in the missing one.
3. This process is done feature by feature.

#### Key Parameters:
- `n_neighbors`: Number of neighbors to consider (default = 5)
- `weights`: `'uniform'` or `'distance'` (closer neighbors have more influence)
- `metric`: Distance metric to use (default = `'nan_euclidean'`)

#### Example Usage:
```python
from sklearn.impute import KNNImputer

knn_imputer = KNNImputer(n_neighbors=5, weights='distance')
X_imputed = knn_imputer.fit_transform(X)
```

**Advantages** ✅:
- More accurate than SimpleImputer because it considers feature relationships
- Preserves data structure better
- Works well for both numeric and (after encoding) categorical data

**Disadvantages** ❌:
- Much slower than SimpleImputer (especially on large datasets)
- Requires scaling features beforehand (distance-based)
- Can be memory intensive

---

## Model Evaluation Metrics 📏

Evaluating model performance is crucial in machine learning. Scikit-learn provides comprehensive tools in `sklearn.metrics` to assess how well your models are performing.

---

### Classification Metrics

#### 1. Accuracy
**Accuracy** is the simplest metric. It measures the proportion of correct predictions out of all predictions.

**Formula:**
$$
\text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}}
$$

**Limitation**: Can be misleading with imbalanced datasets.

---

#### 2. Confusion Matrix
A **Confusion Matrix** is a table that summarizes the performance of a classification model by showing the counts of:
- True Positives (TP)
- True Negatives (TN)
- False Positives (FP)
- False Negatives (FN)

It forms the foundation for many other metrics.

---

#### 3. Precision
**Precision** answers: *Of all instances predicted as positive, how many are actually positive?*

**Formula:**
$$
\text{Precision} = \frac{TP}{TP + FP}
$$

Useful when the cost of false positives is high (e.g., spam detection).

---

#### 4. Recall (Sensitivity / True Positive Rate)
**Recall** answers: *Of all actual positive instances, how many were correctly predicted?*

**Formula:**
$$
\text{Recall} = \frac{TP}{TP + FN}
$$

Important when the cost of false negatives is high (e.g., disease detection).

---

#### 5. F1 Score
**F1 Score** is the **harmonic mean** of Precision and Recall. It provides a single score that balances both metrics.

**Formula:**
$$
\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$

Best used when you need a balance between Precision and Recall.

---

#### 6. Classification Report
`classification_report` in scikit-learn gives a comprehensive summary including **Precision**, **Recall**, **F1 Score**, and **Support** (number of samples per class) for each class, along with averages.

---

### Regression Metrics

#### 7. Mean Absolute Error (MAE)
**MAE** measures the average magnitude of errors in predictions without considering their direction.

**Formula:**
$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

**Interpretation**: More robust to outliers than MSE.

---

#### 8. Mean Squared Error (MSE)
**MSE** measures the average of the squared differences between actual and predicted values.

**Formula:**
$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

**Note**: Squaring penalizes large errors more heavily.

---

#### 9. R² Score (Coefficient of Determination)
**R²** tells us how well the model explains the variance in the target variable.

**Formula:**
$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

**Interpretation**:
- R² = 1 → Perfect predictions
- R² = 0 → Model is no better than predicting the mean
- Negative R² → Model is worse than the mean predictor

---

### Clustering Metrics

#### 10. Silhouette Score
**Silhouette Score** measures how similar a point is to its own cluster compared to other clusters. It evaluates clustering quality.

**Formula** (for a single sample):
$$
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
$$

Where:
- $a(i)$ = average distance to other points in the same cluster
- $b(i)$ = average distance to points in the nearest neighboring cluster

**Range**: -1 to +1 (higher is better).
---

### Precision-Recall Curve

The **Precision-Recall Curve** shows the trade-off between **Precision** and **Recall** at different classification thresholds. It is especially useful for **imbalanced datasets**, where the positive class is rare.

- **High Precision** → Fewer false positives
- **High Recall** → Fewer false negatives

#### Example using `cross_val_predict` with `decision_function`:

```python
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import precision_recall_curve, PrecisionRecallDisplay
import matplotlib.pyplot as plt

# Get decision scores instead of predicted classes
y_scores = cross_val_predict(model, X_train, y_train, 
                             cv=5, 
                             method="decision_function")   # or 'predict_proba'[:, 1]

# Compute precision, recall, and thresholds
precisions, recalls, thresholds = precision_recall_curve(y_train, y_scores)

# Plot the curve
plt.figure(figsize=(8, 6))
plt.plot(recalls, precisions, linewidth=2)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.grid(True)
plt.show()
```

You can also use `PrecisionRecallDisplay.from_predictions()` for easier visualization.

---

### ROC Curve & AUC-ROC Score

The **ROC Curve** (Receiver Operating Characteristic) plots the **True Positive Rate (Recall)** against the **False Positive Rate** at various threshold settings.

- **True Positive Rate (TPR)** = Recall = TP / (TP + FN)
- **False Positive Rate (FPR)** = FP / (FP + TN)

#### AUC-ROC Score (Area Under the ROC Curve)
**AUC** measures the **overall ability** of the model to distinguish between classes:
- AUC = 1.0 → Perfect classifier
- AUC = 0.5 → Random guessing (no discrimination)
- AUC < 0.5 → Worse than random

#### Example:

```python
from sklearn.metrics import roc_curve, roc_auc_score, RocCurveDisplay

# Using decision scores from cross_val_predict
y_scores = cross_val_predict(model, X_train, y_train, 
                             cv=5, 
                             method="decision_function")

fpr, tpr, thresholds = roc_curve(y_train, y_scores)
auc_score = roc_auc_score(y_train, y_scores)

# Plot ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, linewidth=2, label=f'AUC = {auc_score:.3f}')
plt.plot([0, 1], [0, 1], 'k--')  # Random classifier line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()
```

---

## When to Use Which Curve?

- **Precision-Recall Curve**: Preferred when dealing with **imbalanced classes** (focuses on the positive class).
- **ROC Curve**: Better when classes are roughly balanced or you care about overall ranking ability.

**AUC-ROC** is one of the most widely reported metrics for binary classification performance.

---

## Data Preprocessing with `sklearn.preprocessing` 🔧

Preprocessing is a critical step in any machine learning pipeline. Scikit-learn provides excellent tools to transform and prepare data before feeding it to models.

---

### Scaling and Normalization

#### 1. StandardScaler
**StandardScaler** standardizes features by removing the mean and scaling to unit variance (z-score normalization).

It transforms each feature to have:
- Mean = 0
- Standard deviation = 1

**Best for**: Algorithms that assume data is normally distributed (e.g., Logistic Regression, SVM, Neural Networks).

---

#### 2. MinMaxScaler
**MinMaxScaler** scales each feature to a fixed range, usually between 0 and 1.

It transforms values using the minimum and maximum values of each feature.

**Best for**: Algorithms that require bounded input (e.g., Neural Networks, KNN, image data).

---

#### 3. RobustScaler
**RobustScaler** scales features using statistics that are robust to outliers (median and Interquartile Range).

It subtracts the median and scales by the IQR (75th percentile - 25th percentile).

**Best for**: Datasets containing many outliers.

---

#### 4. Normalizer
**Normalizer** scales each **sample** (row) to have unit norm (length = 1).

It works on individual samples rather than features. Common norms are L1 (Manhattan) and L2 (Euclidean).

**Best for**: Text data or when the direction of the vector matters more than its magnitude.

---

### Encoding Categorical Variables

#### 5. OneHotEncoder
**OneHotEncoder** converts categorical features into a set of binary (0/1) columns, with one column per unique category.

It creates sparse or dense binary vectors. Avoids implying any ordinal relationship between categories.

**Important**: Use `drop='first'` to avoid the dummy variable trap.

---

#### 6. OrdinalEncoder
**OrdinalEncoder** encodes categorical features as integers based on their order.

It assigns increasing integers to categories (e.g., low=0, medium=1, high=2).

**Best for**: Ordinal data where the order has meaning.

---

#### 7. LabelEncoder
**LabelEncoder** converts categorical labels (target variable) into integer values (0 to n_classes-1).

It is mainly used for the **target variable** in classification tasks, not for input features.

---

### Feature Engineering

#### 8. PolynomialFeatures
**PolynomialFeatures** generates polynomial and interaction terms from existing features.

For example, from features [a, b], it can create [1, a, b, a², ab, b²], etc.

**Useful for**: Capturing non-linear relationships when using linear models.

---

#### 9. FunctionTransformer
**FunctionTransformer** allows you to apply any custom Python function to your data as part of a scikit-learn pipeline.

It makes custom transformations (e.g., log transform, square root, custom scaling) compatible with Pipelines.

---

## Model Selection & Evaluation with `sklearn.model_selection` 🔍

The `sklearn.model_selection` module provides essential tools for **splitting data**, **evaluating models**, **avoiding overfitting/underfitting**, and **tuning hyperparameters**. It helps you select the best model and its optimal configuration for your dataset.

---

### 1. `train_test_split`
**`train_test_split`** is the most basic and widely used function to split your data into training and testing sets. It is used in almost every machine learning project.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42, 
    stratify=y          # Maintain class distribution (good for classification)
)
```

---

### 2. `cross_val_score`
**`cross_val_score`** evaluates a model using **Cross-Validation**. It trains and scores the model on multiple folds and returns the scores for each fold.

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
scores = cross_val_score(model, X, y, cv=5, scoring='f1')  # or 'accuracy', 'roc_auc', etc.

print("Cross-validation scores:", scores)
print("Mean score:", scores.mean())
```

---

### 3. `cross_val_predict`
**`cross_val_predict`** returns the predictions made during cross-validation. It is very useful when you need prediction scores (e.g., for ROC or Precision-Recall curves).

```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
y_scores = cross_val_predict(model, X, y, cv=5, method="decision_function")
```

---

### 4. `KFold` and `StratifiedKFold`
These classes give you fine-grained control over cross-validation splits.

- **`KFold`**: For regression or when class balance is not important.
- **`StratifiedKFold`**: For classification (preserves class proportions).

```python
from sklearn.model_selection import KFold, StratifiedKFold

# For regression
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# For classification (recommended)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

for train_idx, val_idx in skf.split(X, y):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
```

---

### 5. `GridSearchCV`
**`GridSearchCV`** performs exhaustive hyperparameter tuning by trying all possible combinations.

```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

param_grid = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

grid_search = GridSearchCV(
    SVC(), 
    param_grid, 
    cv=5, 
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Best score:", grid_search.best_score_)
print("Best estimator:", grid_search.best_estimator_)
```

---

### 6. `RandomizedSearchCV`
**`RandomizedSearchCV`** searches randomly through the parameter space. It is faster and often more efficient than Grid Search.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC
from scipy.stats import uniform, randint

param_dist = {
    'C': uniform(0.1, 100),
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

random_search = RandomizedSearchCV(
    SVC(), 
    param_dist, 
    n_iter=20,      # Number of random combinations to try
    cv=5, 
    scoring='accuracy',
    random_state=42,
    n_jobs=-1
)

random_search.fit(X_train, y_train)

print("Best parameters:", random_search.best_params_)
print("Best score:", random_search.best_score_)
```

---

### 7. `learning_curve`
**`learning_curve`** helps diagnose underfitting and overfitting by showing how performance changes with training set size.

```python
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import numpy as np

train_sizes, train_scores, val_scores = learning_curve(
    model, X, y, 
    cv=5, 
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy'
)

plt.plot(train_sizes, train_scores.mean(axis=1), label='Training Score')
plt.plot(train_sizes, val_scores.mean(axis=1), label='Validation Score')
plt.xlabel('Training Set Size')
plt.ylabel('Score')
plt.legend()
plt.title('Learning Curve')
plt.show()
```

---

### 8. `validation_curve`
**`validation_curve`** shows how a model’s performance changes with respect to **one specific hyperparameter**.

```python
from sklearn.model_selection import validation_curve

param_range = [0.001, 0.01, 0.1, 1, 10, 100]

train_scores, val_scores = validation_curve(
    SVC(), X, y,
    param_name='C',
    param_range=param_range,
    cv=5,
    scoring='accuracy'
)

plt.plot(param_range, train_scores.mean(axis=1), label='Training Score')
plt.plot(param_range, val_scores.mean(axis=1), label='Validation Score')
plt.xlabel('C (Regularization Parameter)')
plt.ylabel('Score')
plt.legend()
plt.title('Validation Curve')
plt.show()
```

---

## Pipelines & ColumnTransformer 🔄

### 1. Pipeline
**`Pipeline`** allows you to chain multiple data processing steps and a final estimator into a single object. 

It ensures that the same transformations are applied consistently during training and prediction, and helps prevent **data leakage**.

**Main Benefits**:
- Cleaner and more maintainable code
- Easier cross-validation and hyperparameter tuning
- Prevents mistakes (e.g., fitting on test data)

---

### 2. ColumnTransformer
**`ColumnTransformer`** is used to apply **different preprocessing steps** to **different columns** of your dataset.

It is especially useful when your data contains both numerical and categorical features that require different transformations (e.g., scaling for numbers, one-hot encoding for categories).

**Key Advantages**:
- Handles mixed data types elegantly
- Works perfectly inside a `Pipeline`
- Keeps your preprocessing organized and reproducible

---

### Typical Usage Pattern

You usually combine both:

- Use `ColumnTransformer` for preprocessing different column types.
- Put everything (including the model) inside a `Pipeline`.

This combination is considered best practice in scikit-learn for building robust machine learning workflows.

---

## Feature Engineering Cheat Sheet 💡

Feature Engineering is often the most important factor in building high-performing models. Good features can dramatically improve results more than choosing a complex algorithm.

### General Best Practices

- **Domain Knowledge is King**: Always try to create features based on **business understanding** of the problem.
- Create features that are **interpretable** and meaningful.
- Handle missing values, outliers, and data types before creating new features.
- Test new features using cross-validation to ensure they actually improve performance.

---

### Scaling Guidelines

| Model Type                  | Needs Scaling? | Recommended Scaler          |
|-----------------------------|----------------|-----------------------------|
| Distance-based (KNN, SVM, Neural Nets, K-Means, DBSCAN) | **Yes**        | `StandardScaler` or `MinMaxScaler` |
| Tree-based (Random Forest, XGBoost, LightGBM)           | **No**         | Not required                |
| Linear Models (Logistic, Ridge, Lasso)                  | Recommended    | `StandardScaler`            |
| PCA, LDA, t-SNE             | **Yes**        | `StandardScaler`            |

**Tip**: When in doubt, scale numerical features.

---

### Powerful Feature Engineering Techniques

#### 1. Mathematical Transformations
- **Ratios** and proportions (e.g., `price_per_sqft = price / area`)
- **Differences** (e.g., `age_diff = age_current - age_start`)
- **Log transform** for skewed data (`np.log1p(feature)`)
- **Polynomial / Interaction terms** (use `PolynomialFeatures` carefully)

#### 2. Tree Models Specific Tips
- Tree-based models (Random Forest, XGBoost, etc.) can learn non-linear relationships automatically.
- They **love** raw features + **ratios** and **group statistics**.
- Creating **interaction features** manually is often still beneficial.
- Binning continuous variables into categories can sometimes help.

#### 3. Business / Domain-Based Features
- **Aggregations**: Mean, sum, max, min, count per group (e.g., average transaction per customer)
- **Time-based features**: Day of week, month, is_weekend, time since last event
- **Frequency / Count features**: How many times something occurred
- **Flag features**: Binary indicators (e.g., `has_discount`, `is_new_customer`)
- **Target Encoding** (careful with leakage): Replace categories with mean target value

---

### Quick Tips for Success

- **Start simple**: Begin with raw features + basic preprocessing, then iteratively add engineered features.
- **Avoid leakage**: Never use test data or future information when creating features.
- **Dimensionality**: Too many features can cause overfitting and slow training — use feature selection or dimensionality reduction when needed.
- **Validate**: Always check if a new feature improves your cross-validation score.
- Combine **automated** feature engineering (e.g., PolynomialFeatures) with **manual domain-driven** features.

---

**Pro Tip**: The best features are usually the ones that reflect real-world business logic rather than purely mathematical transformations.
