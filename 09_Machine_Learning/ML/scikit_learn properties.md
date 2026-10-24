# 📦 scikit-learn Properties & Key Modules

A practical reference to the most-used scikit-learn modules, arranged in the order you would use them in a typical workflow: **prepare the data → build pipelines → select and tune models → evaluate results**.

<a id="contents"></a>
## 📚 Contents

1. [Handling Missing Values with `sklearn.impute` 🩹](#imp)
   - [SimpleImputer 🧼](#imp-simpleimputer)
   - [KNNImputer 🧑‍🤝‍🧑](#imp-knnimputer)

2. [Data Preprocessing with `sklearn.preprocessing` 🔧](#prep)
   - [StandardScaler](#prep-standardscaler)
   - [MinMaxScaler](#prep-minmaxscaler)
   - [RobustScaler](#prep-robustscaler)
   - [Normalizer](#prep-normalizer)
   - [OneHotEncoder](#prep-onehotencoder)
   - [OrdinalEncoder](#prep-ordinalencoder)
   - [LabelEncoder](#prep-labelencoder)
   - [PolynomialFeatures](#prep-polynomialfeatures)
   - [FunctionTransformer](#prep-functiontransformer)

3. [Pipelines & ColumnTransformer 🔄](#pipe)
   - [Pipeline](#pipe-pipeline)
   - [ColumnTransformer](#pipe-columntransformer)
   - [Typical Usage Pattern](#pipe-typical-usage-pattern)

4. [Model Selection with `sklearn.model_selection` 🔍](#ms)
   - [`train_test_split`](#ms-train_test_split)
   - [`cross_val_score`](#ms-cross_val_score)
   - [`cross_val_predict`](#ms-cross_val_predict)
   - [`KFold` and `StratifiedKFold`](#ms-kfold-and-stratifiedkfold)
   - [`GridSearchCV`](#ms-gridsearchcv)
   - [`RandomizedSearchCV`](#ms-randomizedsearchcv)
   - [`learning_curve`](#ms-learning_curve)
   - [`validation_curve`](#ms-validation_curve)

5. [Model Evaluation Metrics 📏](#met)
   - [Classification Metrics](#met-classification-metrics)
      - [Accuracy](#met-accuracy)
      - [Confusion Matrix](#met-confusion-matrix)
      - [Precision](#met-precision)
      - [Recall (Sensitivity / True Positive Rate)](#met-recall-sensitivity-true-positive-rate)
      - [F1 Score](#met-f1-score)
      - [Classification Report](#met-classification-report)
   - [Regression Metrics](#met-regression-metrics)
      - [Mean Absolute Error (MAE)](#met-mean-absolute-error-mae)
      - [Mean Squared Error (MSE)](#met-mean-squared-error-mse)
      - [R² Score (Coefficient of Determination)](#met-r-score-coefficient-of-determination)
   - [Clustering Metrics](#met-clustering-metrics)
      - [Silhouette Score](#met-silhouette-score)
   - [Classification Curves](#met-classification-curves)
      - [Precision-Recall Curve](#met-precision-recall-curve)
      - [ROC Curve & AUC-ROC Score](#met-roc-curve-auc-roc-score)
      - [When to Use Which Curve?](#met-when-to-use-which-curve)

6. [Feature Engineering Cheat Sheet 💡](#fe)
   - [General Best Practices](#fe-general-best-practices)
   - [Scaling Guidelines](#fe-scaling-guidelines)
   - [Powerful Feature Engineering Techniques](#fe-powerful-feature-engineering-techniques)
   - [Quick Tips for Success](#fe-quick-tips-for-success)

---

## 🧭 Modules at a Glance

| # | Module | Purpose | Key tools |
|---|--------|---------|-----------|
| 1 | [`sklearn.impute`](#imp) | Fill in missing values | `SimpleImputer`, `KNNImputer` |
| 2 | [`sklearn.preprocessing`](#prep) | Scale, encode, and engineer features | `StandardScaler`, `OneHotEncoder`, `PolynomialFeatures`, … |
| 3 | [`sklearn.pipeline` / `sklearn.compose`](#pipe) | Chain steps and treat columns differently | `Pipeline`, `ColumnTransformer` |
| 4 | [`sklearn.model_selection`](#ms) | Split, cross-validate, tune, and diagnose | `train_test_split`, `GridSearchCV`, `learning_curve`, … |
| 5 | [`sklearn.metrics`](#met) | Measure model quality | `classification_report`, `roc_auc_score`, `r2_score`, … |
| 6 | [Feature Engineering Cheat Sheet](#fe) | Practical guidance for better features | n/a |

---

<a id="imp"></a>
## 1. Handling Missing Values with `sklearn.impute` 🩹

Missing data is a common problem in real-world datasets. The `sklearn.impute` module provides two tools for filling in missing values (NaN).

| | SimpleImputer | KNNImputer |
|---|---------------|------------|
| **Approach** | Column-wise statistic or constant | Average of the K most similar samples |
| **Uses relationships between features** | No | Yes |
| **Speed** | Very fast | Slower, especially on large datasets |
| **Needs feature scaling** | No | Yes (distance-based) |
| **Good for** | Baselines and quick pipelines | Higher-quality imputation on small to medium data |

<a id="imp-simpleimputer"></a>
### SimpleImputer 🧼

**SimpleImputer** is a fast, straightforward way to replace missing values with a constant or a statistic calculated from the available data in each column.

#### Strategies

| Strategy | Replaces missing values with | Best for |
|----------|------------------------------|----------|
| `'mean'` | The column **mean** | Numeric data |
| `'median'` | The column **median** | Numeric data with outliers |
| `'most_frequent'` | The **mode** | Categorical data |
| `'constant'` | A fixed value set with `fill_value` (e.g., 0 or -1) | When "missing" has its own meaning |

#### Example

```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')     # or 'median', 'most_frequent', 'constant'
imputer.fit(X_train)                         # learn the statistics from the training data only
X_train_imputed = imputer.transform(X_train)
X_test_imputed = imputer.transform(X_test)   # reuse the training statistics on the test data
```

| ✅ Advantages | ❌ Disadvantages |
|--------------|-----------------|
| Very fast and simple | Ignores relationships between features |
| Easy to interpret | Can distort the data distribution when many values are missing |
| Works well as a baseline | |

<a id="imp-knnimputer"></a>
### KNNImputer 🧑‍🤝‍🧑

**KNNImputer** uses the **K-Nearest Neighbors** algorithm to fill missing values by looking at similar samples.

#### How It Works

1. For each missing value, find the **K nearest neighbors** (measured on the other features).
2. Fill the gap with the average (or distance-weighted average) of those neighbors' values.
3. Repeat feature by feature.

#### Key Parameters

| Parameter | Meaning | Default |
|-----------|---------|---------|
| `n_neighbors` | Number of neighbors to consider | `5` |
| `weights` | `'uniform'`, or `'distance'` (closer neighbors have more influence) | `'uniform'` |
| `metric` | Distance metric | `'nan_euclidean'` |

#### Example

```python
from sklearn.impute import KNNImputer

knn_imputer = KNNImputer(n_neighbors=5, weights='distance')
X_imputed = knn_imputer.fit_transform(X)
```

> 💡 To avoid data leakage, fit the imputer on the training data only and call `transform` on the test data, as in the `SimpleImputer` example.

| ✅ Advantages | ❌ Disadvantages |
|--------------|-----------------|
| More accurate than SimpleImputer because it uses feature relationships | Much slower than SimpleImputer, especially on large datasets |
| Preserves data structure better | Requires scaling features beforehand (distance-based) |
| Works for numeric data and, after encoding, categorical data | Can be memory intensive |

[↑ Back to contents](#contents)

---

<a id="prep"></a>
## 2. Data Preprocessing with `sklearn.preprocessing` 🔧

Preprocessing is a critical step in any machine learning pipeline. The `sklearn.preprocessing` module transforms raw data into a form models can use.

| Tool | Category | Purpose |
|------|----------|---------|
| [`StandardScaler`](#prep-standardscaler) | Scaling | Zero mean, unit variance |
| [`MinMaxScaler`](#prep-minmaxscaler) | Scaling | Fixed range, usually 0 to 1 |
| [`RobustScaler`](#prep-robustscaler) | Scaling | Median and IQR, robust to outliers |
| [`Normalizer`](#prep-normalizer) | Scaling | Unit length per sample (row) |
| [`OneHotEncoder`](#prep-onehotencoder) | Encoding | One binary column per category |
| [`OrdinalEncoder`](#prep-ordinalencoder) | Encoding | Integers that respect category order |
| [`LabelEncoder`](#prep-labelencoder) | Encoding | Integer codes for the target variable |
| [`PolynomialFeatures`](#prep-polynomialfeatures) | Feature engineering | Polynomial and interaction terms |
| [`FunctionTransformer`](#prep-functiontransformer) | Feature engineering | Any custom function inside a pipeline |

> ⚠️ **Always fit on the training data only**, then reuse the fitted object on the test data:
>
> ```python
> scaler = StandardScaler()
> X_train_scaled = scaler.fit_transform(X_train)   # learn parameters from the training data
> X_test_scaled = scaler.transform(X_test)         # apply the same parameters to the test data
> ```

<a id="prep-standardscaler"></a>
### StandardScaler

**StandardScaler** standardizes features by removing the mean and scaling to unit variance (z-score normalization):

$$
z = \frac{x - \mu}{\sigma}
$$

Each feature ends up with a mean of 0 and a standard deviation of 1.

**Best for**: Scale-sensitive algorithms such as Logistic Regression, SVM, KNN, Neural Networks, and PCA.

**Watch out**: Outliers affect the mean and standard deviation. Use `RobustScaler` if you have many.

<a id="prep-minmaxscaler"></a>
### MinMaxScaler

**MinMaxScaler** rescales each feature to a fixed range, usually 0 to 1, using the feature's minimum and maximum:

$$
x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$$

**Best for**: Algorithms that need bounded input or are distance-based (e.g., Neural Networks, KNN, image data).

**Watch out**: A single extreme outlier compresses all other values into a narrow band.

<a id="prep-robustscaler"></a>
### RobustScaler

**RobustScaler** scales features with statistics that are robust to outliers: it subtracts the **median** and divides by the **interquartile range** (IQR = 75th percentile − 25th percentile).

**Best for**: Datasets that contain many outliers.

<a id="prep-normalizer"></a>
### Normalizer

**Normalizer** rescales each **sample** (row) to unit norm (length = 1). Unlike the scalers above, it works on rows rather than columns. Common norms are L1 (Manhattan) and L2 (Euclidean).

**Best for**: Text data, or any case where the direction of the vector matters more than its magnitude.

<a id="prep-onehotencoder"></a>
### OneHotEncoder

**OneHotEncoder** converts a categorical feature into binary (0/1) columns, one per unique category. It does not imply any order between categories.

**Useful options**:
- `drop='first'`: drops one column per feature to avoid the dummy variable trap (multicollinearity). This matters mainly for linear models.
- `handle_unknown='ignore'`: prevents errors when the test data contains categories not seen in training.

<a id="prep-ordinalencoder"></a>
### OrdinalEncoder

**OrdinalEncoder** encodes categorical features as integers that follow a meaningful order (e.g., low = 0, medium = 1, high = 2).

**Best for**: Ordinal data, where the order has meaning.

**Watch out**: By default, categories are ordered alphabetically. Pass `categories=[['low', 'medium', 'high']]` to set the real order.

<a id="prep-labelencoder"></a>
### LabelEncoder

**LabelEncoder** converts class labels into integers from 0 to `n_classes - 1`.

It is meant for the **target variable** (`y`) in classification, not for input features.

<a id="prep-polynomialfeatures"></a>
### PolynomialFeatures

**PolynomialFeatures** generates polynomial and interaction terms from existing features. For example, from features `[a, b]` with degree 2 it creates `[1, a, b, a², ab, b²]`.

**Useful for**: Capturing non-linear relationships with linear models.

<a id="prep-functiontransformer"></a>
### FunctionTransformer

**FunctionTransformer** applies any custom Python function to your data and makes it compatible with scikit-learn pipelines (e.g., log transform, square root, custom scaling).

```python
import numpy as np
from sklearn.preprocessing import FunctionTransformer

log_transformer = FunctionTransformer(np.log1p)   # log(1 + x), handy for skewed data
```

[↑ Back to contents](#contents)

---

<a id="pipe"></a>
## 3. Pipelines & ColumnTransformer 🔄

These two tools turn preprocessing and modeling into one reproducible workflow.

| Tool | Purpose | Key benefit |
|------|---------|-------------|
| `Pipeline` | Chain processing steps and a final estimator into one object | Consistent transformations; prevents data leakage |
| `ColumnTransformer` | Apply **different** preprocessing steps to **different** columns | Handles mixed numeric and categorical data |

<a id="pipe-pipeline"></a>
### Pipeline

**`Pipeline`** chains multiple processing steps and a final estimator into a single object.

It applies the same transformations during training and prediction, and helps prevent **data leakage**.

**Main benefits**:
- Cleaner, more maintainable code
- Easier cross-validation and hyperparameter tuning
- Prevents mistakes such as fitting on test data

<a id="pipe-columntransformer"></a>
### ColumnTransformer

**`ColumnTransformer`** applies different preprocessing steps to different columns of your dataset.

It is especially useful when your data mixes numerical and categorical features that need different treatment (e.g., scaling for numbers, one-hot encoding for categories).

**Key advantages**:
- Handles mixed data types cleanly
- Works inside a `Pipeline`
- Keeps preprocessing organized and reproducible

<a id="pipe-typical-usage-pattern"></a>
### Typical Usage Pattern

Combine both: use `ColumnTransformer` to preprocess each column type, then put everything, including the model, inside a `Pipeline`. This is considered best practice for robust scikit-learn workflows.

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

numeric_features = ['age', 'income']
categorical_features = ['city', 'gender']

numeric_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler()),
])

categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore')),
])

preprocessor = ColumnTransformer([
    ('num', numeric_pipeline, numeric_features),
    ('cat', categorical_pipeline, categorical_features),
])

model = Pipeline([
    ('preprocess', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000)),
])

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

> 💡 To tune a pipeline with `GridSearchCV`, address parameters as `step__parameter`, for example `classifier__C`.

[↑ Back to contents](#contents)

---

<a id="ms"></a>
## 4. Model Selection with `sklearn.model_selection` 🔍

The `sklearn.model_selection` module provides tools for **splitting data**, **evaluating models**, **diagnosing overfitting and underfitting**, and **tuning hyperparameters**.

| Tool | Purpose |
|------|---------|
| [`train_test_split`](#ms-train_test_split) | Split data into training and test sets |
| [`cross_val_score`](#ms-cross_val_score) | Score a model with cross-validation |
| [`cross_val_predict`](#ms-cross_val_predict) | Get out-of-fold predictions or scores |
| [`KFold` / `StratifiedKFold`](#ms-kfold-and-stratifiedkfold) | Control how cross-validation splits are made |
| [`GridSearchCV`](#ms-gridsearchcv) | Exhaustive hyperparameter search |
| [`RandomizedSearchCV`](#ms-randomizedsearchcv) | Random hyperparameter search (faster) |
| [`learning_curve`](#ms-learning_curve) | Diagnose bias/variance vs. training set size |
| [`validation_curve`](#ms-validation_curve) | Diagnose the effect of a single hyperparameter |

> 📝 The examples below assume `X` (features), `y` (labels), and a scikit-learn estimator named `model` are already defined.

<a id="ms-train_test_split"></a>
### `train_test_split`

The most basic and widely used function: it splits your data into training and test sets. It appears in almost every machine learning project.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y          # keep the class distribution (good for classification)
)
```

<a id="ms-cross_val_score"></a>
### `cross_val_score`

Evaluates a model with **cross-validation**: it trains and scores the model on several folds and returns one score per fold.

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
scores = cross_val_score(model, X, y, cv=5, scoring='f1')   # or 'accuracy', 'roc_auc', etc.

print("Cross-validation scores:", scores)
print("Mean score:", scores.mean())
```

<a id="ms-cross_val_predict"></a>
### `cross_val_predict`

Returns the predictions made for each sample while it was in the validation fold. It is very useful when you need prediction scores, for example for ROC or Precision-Recall curves.

```python
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
y_scores = cross_val_predict(model, X, y, cv=5, method='decision_function')
```

<a id="ms-kfold-and-stratifiedkfold"></a>
### `KFold` and `StratifiedKFold`

These classes give you fine-grained control over cross-validation splits.

| Class | Use for |
|-------|---------|
| `KFold` | Regression, or when class balance is not important |
| `StratifiedKFold` | Classification (preserves class proportions in each fold) |

```python
from sklearn.model_selection import KFold, StratifiedKFold

# For regression
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# For classification (recommended)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# X and y are NumPy arrays here; with pandas use X.iloc[train_idx] and y.iloc[train_idx]
for train_idx, val_idx in skf.split(X, y):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]
```

<a id="ms-gridsearchcv"></a>
### `GridSearchCV`

Performs exhaustive hyperparameter tuning by trying **every combination** in the grid.

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

<a id="ms-randomizedsearchcv"></a>
### `RandomizedSearchCV`

Searches the parameter space **randomly**. It is faster than grid search and often just as effective.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC
from scipy.stats import uniform

param_dist = {
    'C': uniform(0.1, 100),      # sampled from the range 0.1 to 100.1
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

random_search = RandomizedSearchCV(
    SVC(),
    param_dist,
    n_iter=20,                   # number of random combinations to try
    cv=5,
    scoring='accuracy',
    random_state=42,
    n_jobs=-1
)

random_search.fit(X_train, y_train)

print("Best parameters:", random_search.best_params_)
print("Best score:", random_search.best_score_)
```

<a id="ms-learning_curve"></a>
### `learning_curve`

Helps diagnose **underfitting and overfitting** by showing how performance changes with training set size.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

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

<a id="ms-validation_curve"></a>
### `validation_curve`

Shows how a model's performance changes with **one specific hyperparameter**.

```python
import matplotlib.pyplot as plt
from sklearn.model_selection import validation_curve
from sklearn.svm import SVC

param_range = [0.001, 0.01, 0.1, 1, 10, 100]

train_scores, val_scores = validation_curve(
    SVC(), X, y,
    param_name='C',
    param_range=param_range,
    cv=5,
    scoring='accuracy'
)

plt.semilogx(param_range, train_scores.mean(axis=1), label='Training Score')
plt.semilogx(param_range, val_scores.mean(axis=1), label='Validation Score')
plt.xlabel('C (Regularization Parameter)')
plt.ylabel('Score')
plt.legend()
plt.title('Validation Curve')
plt.show()
```

[↑ Back to contents](#contents)

---

<a id="met"></a>
## 5. Model Evaluation Metrics 📏

Evaluating model performance is crucial. The `sklearn.metrics` module provides the tools to measure how well your models perform.

| Metric | Task | Question it answers | Function |
|--------|------|---------------------|----------|
| Accuracy | Classification | What share of predictions is correct? | `accuracy_score` |
| Confusion Matrix | Classification | Which kinds of errors are made? | `confusion_matrix` |
| Precision | Classification | Of the predicted positives, how many are real? | `precision_score` |
| Recall | Classification | Of the real positives, how many were found? | `recall_score` |
| F1 Score | Classification | How balanced are precision and recall? | `f1_score` |
| Classification Report | Classification | All of the above, per class | `classification_report` |
| MAE | Regression | What is the average absolute error? | `mean_absolute_error` |
| MSE | Regression | What is the average squared error? | `mean_squared_error` |
| R² | Regression | How much variance does the model explain? | `r2_score` |
| Silhouette Score | Clustering | How well separated are the clusters? | `silhouette_score` |
| PR Curve | Classification | How do precision and recall trade off across thresholds? | `precision_recall_curve` |
| ROC / AUC | Classification | How well does the model rank positives above negatives? | `roc_curve`, `roc_auc_score` |

<a id="met-classification-metrics"></a>
### Classification Metrics

<a id="met-accuracy"></a>
#### Accuracy

**Accuracy** is the simplest metric: the proportion of correct predictions out of all predictions.

$$
\text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}}
$$

**Limitation**: Can be misleading on imbalanced datasets.

<a id="met-confusion-matrix"></a>
#### Confusion Matrix

A **confusion matrix** summarizes a classification model's performance by counting:

| | Predicted Positive | Predicted Negative |
|---|---|---|
| **Actual Positive** | True Positives (TP) | False Negatives (FN) |
| **Actual Negative** | False Positives (FP) | True Negatives (TN) |

It is the foundation for many other metrics.

<a id="met-precision"></a>
#### Precision

**Precision** answers: *Of all instances predicted as positive, how many are actually positive?*

$$
\text{Precision} = \frac{TP}{TP + FP}
$$

**Use when** the cost of false positives is high (e.g., spam detection).

<a id="met-recall-sensitivity-true-positive-rate"></a>
#### Recall (Sensitivity / True Positive Rate)

**Recall** answers: *Of all actual positive instances, how many were correctly predicted?*

$$
\text{Recall} = \frac{TP}{TP + FN}
$$

**Use when** the cost of false negatives is high (e.g., disease detection).

<a id="met-f1-score"></a>
#### F1 Score

**F1 Score** is the **harmonic mean** of Precision and Recall, giving a single score that balances both.

$$
\text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$

**Use when** you need a balance between Precision and Recall.

<a id="met-classification-report"></a>
#### Classification Report

`classification_report` gives a complete summary for each class: **Precision**, **Recall**, **F1 Score**, and **Support** (the number of samples in the class), plus overall averages.

```python
from sklearn.metrics import confusion_matrix, classification_report

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

<a id="met-regression-metrics"></a>
### Regression Metrics

<a id="met-mean-absolute-error-mae"></a>
#### Mean Absolute Error (MAE)

**MAE** is the average magnitude of the errors, ignoring their direction.

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

**Interpretation**: More robust to outliers than MSE.

<a id="met-mean-squared-error-mse"></a>
#### Mean Squared Error (MSE)

**MSE** is the average of the squared differences between actual and predicted values.

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

**Note**: Squaring penalizes large errors more heavily.

<a id="met-r-score-coefficient-of-determination"></a>
#### R² Score (Coefficient of Determination)

**R²** shows how much of the variance in the target variable the model explains.

$$
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
$$

**Interpretation**:
- R² = 1 → Perfect predictions
- R² = 0 → No better than always predicting the mean
- R² < 0 → Worse than predicting the mean

<a id="met-clustering-metrics"></a>
### Clustering Metrics

<a id="met-silhouette-score"></a>
#### Silhouette Score

**Silhouette Score** measures how similar a point is to its own cluster compared with other clusters. It evaluates clustering quality.

**Formula** (for a single sample):

$$
s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}
$$

Where:
- $a(i)$ = average distance to the other points in the same cluster
- $b(i)$ = average distance to the points in the nearest neighboring cluster

**Range**: −1 to +1 (higher is better).

<a id="met-classification-curves"></a>
### Classification Curves

> 📝 The examples in this section assume **binary classification**, with `X_train` and `y_train` already defined.

<a id="met-precision-recall-curve"></a>
#### Precision-Recall Curve

The **Precision-Recall Curve** shows the trade-off between **Precision** and **Recall** across classification thresholds. It is especially useful for **imbalanced datasets**, where the positive class is rare.

- **High Precision** → Fewer false positives
- **High Recall** → Fewer false negatives

**Example using `cross_val_predict` with `decision_function`:**

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import precision_recall_curve

model = LogisticRegression(max_iter=1000)

# Get decision scores instead of predicted classes
y_scores = cross_val_predict(model, X_train, y_train, cv=5,
                             method='decision_function')
# Alternative: method='predict_proba', then use y_scores[:, 1]

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

> 💡 `PrecisionRecallDisplay.from_predictions()` gives you the same plot in one call.

<a id="met-roc-curve-auc-roc-score"></a>
#### ROC Curve & AUC-ROC Score

The **ROC Curve** (Receiver Operating Characteristic) plots the **True Positive Rate (Recall)** against the **False Positive Rate** across threshold settings.

- **True Positive Rate (TPR)** = Recall = TP / (TP + FN)
- **False Positive Rate (FPR)** = FP / (FP + TN)

**AUC** (Area Under the ROC Curve) measures the model's **overall ability** to distinguish between classes:

| AUC | Meaning |
|-----|---------|
| 1.0 | Perfect classifier |
| 0.5 | Random guessing (no discrimination) |
| < 0.5 | Worse than random |

**Example:**

```python
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_curve, roc_auc_score

model = LogisticRegression(max_iter=1000)

# Decision scores from cross-validation
y_scores = cross_val_predict(model, X_train, y_train, cv=5,
                             method='decision_function')

fpr, tpr, thresholds = roc_curve(y_train, y_scores)
auc_score = roc_auc_score(y_train, y_scores)

# Plot the ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, linewidth=2, label=f'AUC = {auc_score:.3f}')
plt.plot([0, 1], [0, 1], 'k--')      # random classifier line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()
```

> 💡 `RocCurveDisplay.from_predictions()` is the one-call alternative.

<a id="met-when-to-use-which-curve"></a>
#### When to Use Which Curve?

| Curve | Prefer when | Why |
|-------|-------------|-----|
| **Precision-Recall** | Classes are **imbalanced** | Focuses on the positive class |
| **ROC / AUC** | Classes are roughly balanced, or you care about overall ranking ability | Summarizes performance across all thresholds |

AUC-ROC is one of the most widely reported metrics for binary classification.

[↑ Back to contents](#contents)

---

<a id="fe"></a>
## 6. Feature Engineering Cheat Sheet 💡

Feature engineering is often the most important factor in building high-performing models. Good features can improve results more than choosing a complex algorithm.

<a id="fe-general-best-practices"></a>
### General Best Practices

- **Use domain knowledge**: Build features from your business understanding of the problem.
- Create features that are **interpretable** and meaningful.
- Handle missing values, outliers, and data types before creating new features.
- Test new features with cross-validation to confirm they actually improve performance.

<a id="fe-scaling-guidelines"></a>
### Scaling Guidelines

| Model type | Needs scaling? | Recommended scaler |
|------------|----------------|--------------------|
| Scale-sensitive (KNN, SVM, Neural Nets, K-Means, DBSCAN) | **Yes** | `StandardScaler` or `MinMaxScaler` |
| Tree-based (Random Forest, XGBoost, LightGBM) | **No** | Not required |
| Linear models (Logistic, Ridge, Lasso) | Recommended | `StandardScaler` |
| PCA, t-SNE | **Yes** | `StandardScaler` |

**Tip**: When in doubt, scale numerical features.

<a id="fe-powerful-feature-engineering-techniques"></a>
### Powerful Feature Engineering Techniques

#### 1. Mathematical Transformations

- **Ratios** and proportions (e.g., `price_per_sqft = price / area`)
- **Differences** (e.g., `age_diff = age_current - age_start`)
- **Log transform** for skewed data (`np.log1p(feature)`)
- **Polynomial / interaction terms** (use `PolynomialFeatures` carefully)

#### 2. Tips for Tree-Based Models

- Tree-based models (Random Forest, XGBoost, etc.) learn non-linear relationships automatically.
- They work well with raw features, **ratios**, and **group statistics**.
- Creating **interaction features** manually is often still beneficial.
- Binning continuous variables into categories can sometimes help.

#### 3. Business and Domain-Based Features

- **Aggregations**: Mean, sum, max, min, or count per group (e.g., average transaction per customer)
- **Time-based features**: Day of week, month, `is_weekend`, time since last event
- **Frequency / count features**: How many times something occurred
- **Flag features**: Binary indicators (e.g., `has_discount`, `is_new_customer`)
- **Target encoding** (careful with leakage): Replace categories with the mean target value

<a id="fe-quick-tips-for-success"></a>
### Quick Tips for Success

- **Start simple**: Begin with raw features and basic preprocessing, then add engineered features step by step.
- **Avoid leakage**: Never use test data or future information when creating features.
- **Watch dimensionality**: Too many features can cause overfitting and slow training. Use feature selection or dimensionality reduction when needed.
- **Validate**: Always check whether a new feature improves your cross-validation score.
- **Combine approaches**: Mix automated feature engineering (e.g., `PolynomialFeatures`) with manual, domain-driven features.

> 💡 **Pro tip**: The best features usually reflect real-world business logic rather than purely mathematical transformations.

[↑ Back to contents](#contents)