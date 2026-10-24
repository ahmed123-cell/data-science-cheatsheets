# 📈 Time Series Forecasting

A structured guide to forecasting values that change over time: the core concepts, baseline methods, evaluation, and the main families of forecasting models, from classical statistics to machine learning and deep learning.

<a id="contents"></a>
## 📚 Contents

**Part 1: Foundations**

1. [What is Time Series Forecasting? 🕒](#intro)
   - [Common Examples](#intro-common-examples)
   - [Goal and Techniques](#intro-goal-and-techniques)

2. [Components of a Time Series 🧩](#comp)
   - [1. Trend 📈](#comp-1-trend)
   - [2. Seasonality 🪾](#comp-2-seasonality)
   - [3. Cyclic Patterns ♻️](#comp-3-cyclic-patterns)
   - [4. Noise (Irregular Component / Residuals) ➿](#comp-4-noise-irregular-component-residuals)

3. [Stationarity ⚖️](#stat)
   - [Why Does Stationarity Matter?](#stat-why-does-stationarity-matter)
   - [Types of Non-Stationarity](#stat-types-of-non-stationarity)
   - [Common Tests for Stationarity](#stat-common-tests-for-stationarity)

4. [Autocorrelation 🔁](#acorr)

5. [ACF vs PACF 📊](#acf)
   - [Autocorrelation Function (ACF)](#acf-autocorrelation-function-acf)
   - [Partial Autocorrelation Function (PACF)](#acf-partial-autocorrelation-function-pacf)
   - [Key Differences](#acf-key-differences)
   - [Foundations Recap 🎯](#acf-foundations-recap)

**Part 2: Baselines & Evaluation**

6. [Baseline Models 🧱](#base)
   - [1. Naive Forecasting (Last Value)](#base-1-naive-forecasting-last-value)
   - [2. Historic Average (Mean Forecast)](#base-2-historic-average-mean-forecast)
   - [3. Window Average (Moving Average / Rolling Mean)](#base-3-window-average-moving-average-rolling-mean)
   - [4. Seasonal Naive](#base-4-seasonal-naive)

7. [Forecast Evaluation Metrics 📏](#metrics)
   - [1. MAE (Mean Absolute Error)](#metrics-1-mae-mean-absolute-error)
   - [2. RMSE (Root Mean Squared Error)](#metrics-2-rmse-root-mean-squared-error)
   - [3. MAPE (Mean Absolute Percentage Error)](#metrics-3-mape-mean-absolute-percentage-error)
   - [Which Metric to Use?](#metrics-which-metric-to-use)

8. [Cross-Validation ⏩](#cv)
   - [What is Cross-Validation in Forecasting?](#cv-what-is-cross-validation-in-forecasting)
   - [How It Works](#cv-how-it-works)
   - [Visual Process (Example with Monthly Data)](#cv-visual-process-example-with-monthly-data)
   - [Key Advantages](#cv-key-advantages)
   - [Common Metrics Used](#cv-common-metrics-used)

**Part 3: Forecasting Models**

9. [ARIMA, SARIMA & SARIMAX 🧮](#arima)
   - [ARIMA (Autoregressive Integrated Moving Average)](#arima-arima-autoregressive-integrated-moving-average)
   - [SARIMA (Seasonal ARIMA)](#arima-sarima-seasonal-arima)
   - [SARIMAX (Seasonal ARIMA with eXogenous variables)](#arima-sarimax-seasonal-arima-with-exogenous-variables)
   - [Summary](#arima-summary)

10. [Prophet (by Meta) 🔮](#prophet)
   - [Key Features](#prophet-key-features)
   - [Main Components](#prophet-main-components)
   - [Advantages and Limitations](#prophet-advantages-and-limitations)
   - [Typical Use Cases](#prophet-typical-use-cases)

11. [Machine Learning for Forecasting 🌲](#ml)
   - [Common ML Models for Forecasting](#ml-common-ml-models-for-forecasting)
   - [Strengths and Challenges](#ml-strengths-and-challenges)

12. [LSTM (Long Short-Term Memory) 🧠](#lstm)
   - [Why LSTM?](#lstm-why-lstm)
   - [Advantages and Limitations](#lstm-advantages-and-limitations)
   - [When to Use LSTM](#lstm-when-to-use-lstm)

---

## 🧭 Models at a Glance

| Approach | Type | Best for | Watch out for |
|----------|------|----------|---------------|
| [Baseline models](#base) | Simple benchmarks | A reference point every complex model must beat | They ignore most patterns in the data |
| [ARIMA](#arima-arima-autoregressive-integrated-moving-average) | Classical statistical | Univariate series with trend, no strong seasonality | Needs a stationary series (differencing) |
| [SARIMA](#arima-sarima-seasonal-arima) | Classical statistical | Trend plus clear seasonal patterns | Seasonal period `m` must be chosen well |
| [SARIMAX](#arima-sarimax-seasonal-arima-with-exogenous-variables) | Classical statistical | Series driven by external variables (holidays, promotions, weather) | Needs the external variables available for the forecast period |
| [Prophet](#prophet) | Additive decomposition | Business series with holidays and trend changes, minimal tuning | Sub-hourly data, very short series, overfitting if untuned |
| [Machine learning](#ml) | Supervised learning on lag features | Many features and non-linear relationships | Feature engineering effort and data leakage risk |
| [LSTM](#lstm) | Deep learning (RNN) | High-frequency, complex, multivariate data with lots of history | Data-hungry, expensive, hard to interpret |

---

<a id="intro"></a>
## 1. What is Time Series Forecasting? 🕒

**Time Series Forecasting** is the process of predicting future values of a variable based on historical data points collected over time.

Unlike standard regression problems, time series data has a temporal order: the sequence of observations matters.

<a id="intro-common-examples"></a>
### Common Examples

- Stock prices
- Sales revenue over months
- Weather patterns
- Website traffic
- Electricity demand

<a id="intro-goal-and-techniques"></a>
### Goal and Techniques

The goal is to uncover underlying patterns in the data and use them to make reliable future predictions. Popular techniques include ARIMA, Prophet, LSTM neural networks, and Exponential Smoothing.

[↑ Back to contents](#contents)

---

<a id="comp"></a>
## 2. Components of a Time Series 🧩

A time series can typically be decomposed into several key components:

| Component | What it is | Fixed interval? | Example |
|-----------|------------|-----------------|---------|
| **Trend** 📈 | Long-term direction of the data | n/a | Rising global temperatures |
| **Seasonality** 🪾 | Regular, predictable, calendar-based pattern | Yes | Ice cream sales every summer |
| **Cyclic** ♻️ | Longer fluctuations without a fixed period | No | Economic recessions and expansions |
| **Noise** ➿ | Random, unexplained variation | n/a | Measurement errors |

<a id="comp-1-trend"></a>
### 1. Trend 📈

The **trend** is the long-term movement or direction in the data. It shows whether the series is generally increasing, decreasing, or staying flat over a long period.

- **Upward trend**: Consistent growth (e.g., rising global temperatures).
- **Downward trend**: Consistent decline (e.g., decreasing CD sales over decades).
- **No trend / horizontal**: Data fluctuates around a constant level.

Trends can be linear or nonlinear.

<a id="comp-2-seasonality"></a>
### 2. Seasonality 🪾

**Seasonality** refers to regular, predictable patterns that repeat at fixed intervals (calendar-based).

**Examples:**
- Higher ice cream sales every summer
- Increased retail sales during holidays (December)
- Weekly patterns in website traffic (higher on weekends)

The repeating period is fixed (daily, weekly, monthly, yearly).

<a id="comp-3-cyclic-patterns"></a>
### 3. Cyclic Patterns ♻️

**Cyclic** variations are fluctuations that are **not** of a fixed frequency. They occur over longer periods (usually 2+ years) and are often related to economic or business cycles.

- Unlike seasonality, cycles do not have a fixed, repeating calendar interval.
- Examples: economic recessions and expansions, housing market booms and busts.

<a id="comp-4-noise-irregular-component-residuals"></a>
### 4. Noise (Irregular Component / Residuals) ➿

**Noise** is the random, unpredictable variation in the data that cannot be explained by trend, seasonality, or cycles.

- Also called the **irregular** or **residual** component.
- It represents random shocks, measurement errors, or unforeseen events.
- Good models try to minimize the impact of noise on forecasts.

[↑ Back to contents](#contents)

---

<a id="stat"></a>
## 3. Stationarity ⚖️

**Stationarity** is a crucial property in time series analysis.

A time series is **stationary** if its statistical properties (mean, variance, autocorrelation) remain constant over time.

<a id="stat-why-does-stationarity-matter"></a>
### Why Does Stationarity Matter?

- Many forecasting models (like ARIMA) assume the data is stationary.
- Non-stationary data can lead to spurious results and poor forecasts.

<a id="stat-types-of-non-stationarity"></a>
### Types of Non-Stationarity

- **Trend-stationary**: Becomes stationary once the trend is removed (constant variance around the trend).
- **Difference-stationary**: Requires differencing (subtracting previous values) to become stationary.

<a id="stat-common-tests-for-stationarity"></a>
### Common Tests for Stationarity

| Test | Null hypothesis | Reading the result |
|------|-----------------|--------------------|
| **Augmented Dickey-Fuller (ADF)** | The series is **non-stationary** (has a unit root) | Small p-value (e.g., < 0.05) → likely stationary |
| **KPSS** | The series is **stationary** | Small p-value (e.g., < 0.05) → likely non-stationary |

[↑ Back to contents](#contents)

---

<a id="acorr"></a>
## 4. Autocorrelation 🔁

**Autocorrelation** (also called serial correlation) measures the correlation between a time series and a lagged version of itself.

- It helps identify how past values influence current values.
- High autocorrelation at specific lags often reveals seasonality or other patterns.

**Examples:**
- **Lag 1**: Correlation between today's value and yesterday's value.
- **Lag 12**: Correlation with the value from 12 periods ago (useful for monthly data with yearly seasonality).

[↑ Back to contents](#contents)

---

<a id="acf"></a>
## 5. ACF vs PACF 📊

<a id="acf-autocorrelation-function-acf"></a>
### Autocorrelation Function (ACF)

- Shows the **total correlation** between the series and its lags.
- Includes both **direct** and **indirect** effects.
- Useful for identifying:
  - Overall correlation structure
  - Seasonality (spikes at seasonal lags)
- In ARIMA modeling, ACF helps determine the **MA (Moving Average)** order.

<a id="acf-partial-autocorrelation-function-pacf"></a>
### Partial Autocorrelation Function (PACF)

- Shows the **direct correlation** between the series and its lag, after removing the effects of all intermediate lags.
- Measures the relationship at a specific lag while controlling for shorter lags.
- Useful for identifying the order of autoregressive (**AR**) terms.
- PACF cuts off after the AR order in pure AR processes.

<a id="acf-key-differences"></a>
### Key Differences

| Aspect | ACF | PACF |
|--------|-----|------|
| What it measures | Total correlation with lags | Direct correlation (controlling intermediates) |
| Use in ARIMA | Helps determine **MA** order | Helps determine **AR** order |
| Behavior in AR(p) | Tails off gradually | Cuts off after lag p |
| Behavior in MA(q) | Cuts off after lag q | Tails off gradually |
| Interpretation | Includes indirect effects | Only direct effects |

> 💡 **Visual tip**: Plot both ACF and PACF to identify the best ARIMA model parameters (p, d, q).

<a id="acf-foundations-recap"></a>
### Foundations Recap 🎯

Understanding these concepts is fundamental to effective time series analysis and forecasting:

1. Decompose the series into **Trend + Seasonality + Cyclic + Noise**.
2. Check for **stationarity**.
3. Analyze **autocorrelation** patterns using **ACF** and **PACF**.

Mastering these will help you build more accurate and interpretable forecasting models.

[↑ Back to contents](#contents)

---

<a id="base"></a>
## 6. Baseline Models 🧱

**Baseline models** (also called naïve or benchmark models) are simple forecasting methods used as a reference point. Any complex model should outperform these baselines to be considered useful.

| Baseline | Forecast | Best for |
|----------|----------|----------|
| Naive | The last observed value | Random-walk or highly persistent series |
| Historic average | The mean of all past data | Stationary series without trend or seasonality |
| Window average | The mean of the last *k* values | Series where recent values matter more than old ones |
| Seasonal naive | The value from the same period in the previous season | Strongly seasonal data |

<a id="base-1-naive-forecasting-last-value"></a>
### 1. Naive Forecasting (Last Value)

- The simplest baseline.
- **Forecast** = last observed value.
- Formula: $\hat{y}_{t+1} = y_t$
- Works well for random walk or highly persistent series.
- Often surprisingly hard to beat in financial or volatile data.

<a id="base-2-historic-average-mean-forecast"></a>
### 2. Historic Average (Mean Forecast)

- Uses the average of **all** historical data as the forecast for all future periods.
- Formula: $\hat{y}_{t+h} = \frac{1}{T} \sum_{t=1}^{T} y_t$
- Best for stationary series with no trend or seasonality.
- Ignores any recent changes or patterns.

<a id="base-3-window-average-moving-average-rolling-mean"></a>
### 3. Window Average (Moving Average / Rolling Mean)

- Calculates the average of the most recent **k** observations (window size).
- Formula: $\hat{y}_{t+1} = \frac{1}{k} \sum_{i=0}^{k-1} y_{t-i}$
- More responsive to recent changes than the full historic average.
- Common window sizes: 3, 7, 12, or 30, depending on data frequency.
- Also called the **Simple Moving Average (SMA)**.

<a id="base-4-seasonal-naive"></a>
### 4. Seasonal Naive

- Extension of the naive method that respects seasonality.
- **Forecast** for the next period = value from the same period in the previous season.
- Formula: $\hat{y}_{t+1} = y_{t+1-m}$, where $m$ is the seasonal period.
- Examples:
  - Monthly data with yearly seasonality → use the value from 12 months ago.
  - Daily data with weekly seasonality → use the value from 7 days ago.
- Very effective for strongly seasonal data.

[↑ Back to contents](#contents)

---

<a id="metrics"></a>
## 7. Forecast Evaluation Metrics 📏

The most common metrics used to evaluate time series forecasting models:

| Metric | Measures | Units | Key property |
|--------|--------------|-------|--------------|
| **MAE** | Average absolute error | Same as data | Less sensitive to outliers than RMSE |
| **RMSE** | Square root of average squared error | Same as data | Penalizes large errors more heavily |
| **MAPE** | Average absolute percentage error | Percent | Easy to communicate; fails near zero |

<a id="metrics-1-mae-mean-absolute-error"></a>
### 1. MAE (Mean Absolute Error)

- Measures the average magnitude of errors in the forecasts.
- Formula:

$$
\text{MAE} = \frac{1}{n} \sum_{t=1}^{n} |y_t - \hat{y}_t|
$$

- **Interpretation**: Average error in the same units as the data.
- Less sensitive to outliers than RMSE.

<a id="metrics-2-rmse-root-mean-squared-error"></a>
### 2. RMSE (Root Mean Squared Error)

- Most widely used metric.
- Formula:

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2}
$$

- **Interpretation**: Penalizes large errors more heavily (due to squaring).
- Same units as the original data.

<a id="metrics-3-mape-mean-absolute-percentage-error"></a>
### 3. MAPE (Mean Absolute Percentage Error)

- Expresses errors as percentages.
- Formula:

$$
\text{MAPE} = \frac{100}{n} \sum_{t=1}^{n} \left| \frac{y_t - \hat{y}_t}{y_t} \right|
$$

- **Advantages**: Easy to interpret (e.g., "on average 8% off").
- **Limitations**: Not suitable when actual values are zero or very close to zero.

<a id="metrics-which-metric-to-use"></a>
### Which Metric to Use?

| Situation | Use |
|-----------|-----|
| General understanding of forecast error | **MAE** |
| Large errors are particularly costly | **RMSE** |
| Communicating results to non-technical stakeholders | **MAPE** |

[↑ Back to contents](#contents)

---

<a id="cv"></a>
## 8. Cross-Validation ⏩

<a id="cv-what-is-cross-validation-in-forecasting"></a>
### What is Cross-Validation in Forecasting?

**Time Series Cross-Validation** (also called **Rolling Window Cross-Validation** or **Walk-Forward Validation**) evaluates model performance on sequential data while respecting the temporal order.

Unlike standard k-fold cross-validation used on tabular data, you **cannot** randomly shuffle time series data. Doing so would leak information from the future into the past.

<a id="cv-how-it-works"></a>
### How It Works

| Strategy | Training window | Use when |
|----------|-----------------|----------|
| **Expanding window** (rolling origin) | Grows with each fold | You want to use all history available |
| **Sliding window** (fixed window) | Stays the same size and moves forward | Older data may be less relevant |

#### 1. Expanding Window (Rolling Origin)

- Start with a small initial training set.
- Train the model on the available data.
- Forecast the next few periods (validation window).
- Expand the training window by adding the validation data, then repeat.

#### 2. Sliding Window (Fixed Window)

- Keep the training window size fixed.
- Slide the window forward in time for each fold.

<a id="cv-visual-process-example-with-monthly-data"></a>
### Visual Process (Example with Monthly Data)

**Expanding window:**

```text
Training: [1 → 12]   → Validate: [13 → 15]
Training: [1 → 15]   → Validate: [16 → 18]
Training: [1 → 18]   → Validate: [19 → 21]
```

**Sliding window (fixed size of 12):**

```text
Training: [1 → 12]   → Validate: [13 → 15]
Training: [4 → 15]   → Validate: [16 → 18]
Training: [7 → 18]   → Validate: [19 → 21]
```

<a id="cv-key-advantages"></a>
### Key Advantages

- Provides a more realistic estimate of how the model will perform on future, unseen data.
- Helps detect overfitting to specific time periods.
- Allows calculation of confidence intervals for model performance.

<a id="cv-common-metrics-used"></a>
### Common Metrics Used

- Average MAE, RMSE, or MAPE across all validation folds.

> ⚠️ **Important**: Always maintain chronological order. Never use future data to predict the past.

This method is essential for reliable model selection and hyperparameter tuning in time series projects.

[↑ Back to contents](#contents)

---

<a id="arima"></a>
## 9. ARIMA, SARIMA & SARIMAX 🧮

| Model | Adds | Parameters | Best for |
|-------|------|------------|----------|
| **ARIMA** | Trend handling through differencing | (p, d, q) | Univariate series with trend but no strong seasonality |
| **SARIMA** | Seasonality | (p, d, q)(P, D, Q)m | Series with both trend and clear seasonal patterns |
| **SARIMAX** | External (exogenous) variables | SARIMA + external regressors | Series influenced by outside factors |

<a id="arima-arima-autoregressive-integrated-moving-average"></a>
### ARIMA (Autoregressive Integrated Moving Average)

**ARIMA** is one of the most popular classical statistical models for time series forecasting.

It is defined by three parameters **(p, d, q)**:

| Parameter | Name | Meaning |
|-----------|------|---------|
| **p** (AR) | Autoregressive order | Number of lagged observations used |
| **d** (I) | Integrated order | Number of times the series is differenced to make it stationary |
| **q** (MA) | Moving Average order | Number of lagged forecast errors used |

**Best for**: Univariate time series with trend but no strong seasonality.

<a id="arima-sarima-seasonal-arima"></a>
### SARIMA (Seasonal ARIMA)

**SARIMA** extends ARIMA to handle seasonality.

It uses seven parameters: **(p, d, q)(P, D, Q)m**

- **(p, d, q)**: Non-seasonal parameters (same as ARIMA).
- **(P, D, Q)**: Seasonal parameters (same logic, but applied to seasonal lags).
- **m**: Seasonal period (e.g., 12 for monthly data with yearly seasonality, 7 for daily data with weekly seasonality).

**Best for**: Time series with both trend and clear seasonal patterns.

<a id="arima-sarimax-seasonal-arima-with-exogenous-variables"></a>
### SARIMAX (Seasonal ARIMA with eXogenous variables)

**SARIMAX** is SARIMA plus external (exogenous) variables.

- Lets you include additional predictors (e.g., holidays, promotions, weather, marketing spend).
- Very powerful in real-world scenarios where external factors influence the target variable.

<a id="arima-summary"></a>
### Summary

- **ARIMA** → Basic model (trend only)
- **SARIMA** → Adds seasonality
- **SARIMAX** → Adds external variables

These models are widely implemented in Python through the `statsmodels` library and serve as strong baselines before moving to machine learning or deep learning approaches.

[↑ Back to contents](#contents)

---

<a id="prophet"></a>
## 10. Prophet (by Meta) 🔮

**Prophet** is an open-source forecasting library developed by Facebook (now Meta), designed for business time series data.

<a id="prophet-key-features"></a>
### Key Features

- Easy to use and produces high-quality forecasts with minimal tuning.
- Automatically handles **trend**, **seasonality**, and **holidays**.
- Robust to missing data and outliers.
- Works well with daily, weekly, and monthly data.

<a id="prophet-main-components"></a>
### Main Components

Prophet decomposes the time series into:

| Component | Symbol | Description |
|-----------|--------|-------------|
| **Trend** | $g(t)$ | Non-linear trends with automatic change point detection |
| **Seasonality** | $s(t)$ | Multiple seasonalities (daily, weekly, yearly, custom) |
| **Holidays** | $h(t)$ | User-specified holiday effects |
| **Error term** | $\varepsilon_t$ | Remaining noise |

The model equation:

$$
y(t) = g(t) + s(t) + h(t) + \varepsilon_t
$$

<a id="prophet-advantages-and-limitations"></a>
### Advantages and Limitations

| ✅ Advantages | ❌ Limitations |
|--------------|---------------|
| Very intuitive; requires little statistical expertise | Not ideal for high-frequency data (sub-hourly) |
| Built-in holiday modeling (great for retail and e-commerce) | Less effective for very short time series |
| Handles trend changes and seasonality automatically | Can overfit if not tuned properly |
| Provides uncertainty intervals | |
| Easy to add regressors (similar to SARIMAX) | |

<a id="prophet-typical-use-cases"></a>
### Typical Use Cases

Prophet is especially popular for **business forecasting**, such as:
- Sales and demand forecasting
- Website traffic prediction
- Capacity planning

[↑ Back to contents](#contents)

---

<a id="ml"></a>
## 11. Machine Learning for Forecasting 🌲

**Machine Learning (ML)** approaches treat forecasting as a supervised learning problem by creating lagged features (e.g., previous values, rolling statistics, date features).

<a id="ml-common-ml-models-for-forecasting"></a>
### Common ML Models for Forecasting

- **Tree-based models**: Random Forest, XGBoost, LightGBM, CatBoost (very popular)
- **Regression models**: Linear Regression, Ridge, Lasso
- **K-Nearest Neighbors (KNN)**
- **Support Vector Regression (SVR)**

<a id="ml-strengths-and-challenges"></a>
### Strengths and Challenges

| ✅ Strengths | ❌ Challenges |
|-------------|--------------|
| Handle complex non-linear relationships | Need careful feature engineering (lags, rolling windows, date/time features) |
| Can incorporate many external features easily | Risk of data leakage without proper time series cross-validation |
| Often outperform statistical models when lots of data and features are available | Struggle with long-term forecasting without recursive strategies |
| Good at capturing interactions between variables | |

[↑ Back to contents](#contents)

---

<a id="lstm"></a>
## 12. LSTM (Long Short-Term Memory) 🧠

**LSTM** is a type of **Recurrent Neural Network (RNN)** designed to handle sequential data and long-term dependencies.

<a id="lstm-why-lstm"></a>
### Why LSTM?

- Traditional RNNs suffer from the **vanishing gradient** problem.
- LSTM uses special **gates** (forget, input, output) to selectively remember or forget information over long periods.

<a id="lstm-advantages-and-limitations"></a>
### Advantages and Limitations

| ✅ Advantages in forecasting | ❌ Limitations |
|-----------------------------|---------------|
| Excellent at capturing complex patterns, seasonality, and long-term dependencies | Requires large amounts of data |
| Can model multiple seasonalities and irregular patterns | Computationally expensive and slower to train |
| Works well with multivariate time series | Needs careful hyperparameter tuning and scaling |
| | Often overkill for simple or small datasets |
| | Harder to interpret than ARIMA or Prophet |

<a id="lstm-when-to-use-lstm"></a>
### When to Use LSTM

- High-frequency data (minutes/hours)
- Very complex patterns with long memory
- Multivariate forecasting with many related series
- When you have sufficient historical data (thousands of observations)

> 💡 **Modern alternatives**: Transformer-based models (e.g., Temporal Fusion Transformer, Informer) are increasingly replacing LSTMs in many applications because of better performance and parallel training.

[↑ Back to contents](#contents)