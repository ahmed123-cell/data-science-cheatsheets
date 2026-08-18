<div align='center'>

# Time Series Forecasting

</div>

## 🟦What is Time Series Forecasting?

**Time Series Forecasting** is the process of predicting future values of a variable based on historical data points collected over time. 

Unlike standard regression problems, time series data has a temporal order — the sequence of observations matters. Common examples include:
- Stock prices
- Sales revenue over months
- Weather patterns
- Website traffic
- Electricity demand

The goal is to uncover underlying patterns in the data and use them to make reliable future predictions. Popular techniques include ARIMA, Prophet, LSTM neural networks, and Exponential Smoothing.

---

## 🟦Components of a Time Series

A time series can typically be decomposed into several key components:

### 1. Trend📈
The **trend** represents the long-term movement or direction in the data. It shows whether the series is generally increasing, decreasing, or staying flat over a long period.

- **Upward trend**: Consistent growth (e.g., rising global temperatures).
- **Downward trend**: Consistent decline (e.g., decreasing CD sales over decades).
- **No trend / Horizontal**: Data fluctuates around a constant level.

Trends can be linear or nonlinear.

### 2. Seasonality🪾
**Seasonality** refers to regular, predictable patterns that repeat at fixed intervals (calendar-based).

Examples:
- Higher ice cream sales every summer
- Increased retail sales during holidays (December)
- Weekly patterns in website traffic (higher on weekends)

The repeating period is fixed (daily, weekly, monthly, yearly).

### 3. Cyclic Patterns♻️
**Cyclic** variations are fluctuations that are **not** of a fixed frequency. They occur over longer periods (usually 2+ years) and are often related to economic or business cycles.

- Unlike seasonality, cycles do not have a fixed, repeating calendar interval.
- Examples: Economic recessions and expansions, housing market booms and busts.

### 4. Noise (Irregular Component / Residuals)➿
**Noise** is the random, unpredictable variation in the data that cannot be explained by trend, seasonality, or cycles.

- Also called the **irregular** or **residual** component.
- It represents random shocks, measurement errors, or unforeseen events.
- Good models try to minimize the impact of noise on forecasts.

---

## 🟦Stationarity

**Stationarity** is a crucial property in time series analysis.

A time series is **stationary** if its statistical properties (mean, variance, autocorrelation) remain constant over time.

### Why does stationarity matter?
- Many forecasting models (like ARIMA) assume the data is stationary.
- Non-stationary data can lead to spurious results and poor forecasts.

### Types of non-stationarity:
- **Trend stationarity**: Has a trend but constant variance.
- **Difference stationarity**: Requires differencing (subtracting previous values) to become stationary.

**Common tests for stationarity**: Augmented Dickey-Fuller (ADF) test, KPSS test.

---

## 🟦Autocorrelation

**Autocorrelation** (also called serial correlation) measures the correlation between a time series and a lagged version of itself.

- It helps identify how past values influence current values.
- High autocorrelation at specific lags often reveals seasonality or other patterns.

For example:
- Lag 1 autocorrelation: Correlation between today's value and yesterday's value.
- Lag 12 autocorrelation: Correlation with the value from 12 periods ago (useful for monthly data with yearly seasonality).

---

## 🟦 ACF vs PACF

### Autocorrelation Function (ACF)
- Shows the **total correlation** between the series and its lags.
- Includes both **direct** and **indirect** effects.
- Useful for identifying:
  - Overall correlation structure
  - Seasonality (spikes at seasonal lags)
- In ARIMA modeling, ACF helps determine the **MA (Moving Average)** order.

### Partial Autocorrelation Function (PACF)
- Shows the **direct correlation** between the series and its lag, after removing the effects of all intermediate lags.
- Measures the relationship at a specific lag while controlling for shorter lags.
- Useful for identifying:
  - The order of autoregressive (AR) terms
- PACF cuts off after the AR order in pure AR processes.

### Key Differences:

| Aspect              | ACF                                      | PACF                                      |
|---------------------|------------------------------------------|-------------------------------------------|
| What it measures    | Total correlation with lags              | Direct correlation (controlling intermediates) |
| Use in ARIMA        | Helps determine **MA** order             | Helps determine **AR** order              |
| Behavior in AR(p)   | Tails off gradually                      | Cuts off after lag p                      |
| Behavior in MA(q)   | Cuts off after lag q                     | Tails off gradually                       |
| Interpretation      | Includes indirect effects                | Only direct effects                       |

**Visual Tip**: Plot both ACF and PACF to identify the best ARIMA model parameters (p, d, q).

---

## Summary

Understanding these concepts is fundamental to effective time series analysis and forecasting:
1. Decompose the series into **Trend + Seasonality + Cyclic + Noise**
2. Check for **stationarity**
3. Analyze **autocorrelation** patterns using **ACF** and **PACF**

Mastering these will help you build more accurate and interpretable forecasting models.

---

## 🟦 Baseline Models in Time Series Forecasting

**Baseline models** (also called naïve or benchmark models) are simple forecasting methods used as a reference point. Any complex model should outperform these baselines to be considered useful.

### 1. Naive Forecasting (Last Value)
- The simplest baseline.
- **Forecast** = Last observed value.
- Formula: $(\hat{y}_{t+1} = y_t)$
- Works well for random walk or highly persistent series.
- Often surprisingly hard to beat in financial or volatile data.

### 2. Historic Average (Mean Forecast)
- Uses the average of **all** historical data as the forecast for all future periods.
- **Forecast**: $(\hat{y}_{t+h} = \frac{1}{T} \sum_{t=1}^{T} y_t)$
- Best for stationary series with no trend or seasonality.
- Ignores any recent changes or patterns.

### 3. Window Average (Moving Average / Rolling Mean)
- Calculates the average of the most recent **k** observations (window size).
- **Forecast**: Average of last *k* values.
- More responsive to recent changes than the full historic average.
- Common window sizes: 3, 7, 12, or 30 depending on data frequency.
- Also called **Simple Moving Average (SMA)**.

### 4. Seasonal Naive
- Extension of naive method that respects seasonality.
- **Forecast** for next period = Value from the same period in the previous season.
- Examples:
  - Monthly data with yearly seasonality → Use value from 12 months ago.
  - Daily data with weekly seasonality → Use value from 7 days ago.
- Very effective for strongly seasonal data.

---

## 🟦Forecast Evaluation Metrics

Here are the most common metrics used to evaluate time series forecasting models:

### 1. MAE (Mean Absolute Error)
- Measures the average magnitude of errors in the forecasts.
- Formula:  
  $\text{MAE} = \frac{1}{n} \sum_{t=1}^{n} |y_t - \hat{y}_t|$
- **Interpretation**: Average error in the same units as the data.
- Robust to outliers.

### 2. RMSE (Root Mean Squared Error)
- Most widely used metric.
- Formula:  
  $\text{RMSE} = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (y_t - \hat{y}_t)^2}$
- **Interpretation**: Penalizes large errors more heavily (due to squaring).
- Same units as the original data.

### 3. MAPE (Mean Absolute Percentage Error)
- Expresses errors as percentages.
- Formula:  
  $\text{MAPE} = \frac{100}{n} \sum_{t=1}^{n} \left| \frac{y_t - \hat{y}_t}{y_t} \right|$
- **Advantages**: Easy to interpret (e.g., "on average 8% off").
- **Limitations**: Not suitable when actual values are zero or very close to zero.

---

**Recommendation**:  
Use **MAE** for general understanding, **RMSE** when large errors are particularly costly, and **MAPE** when communicating results to non-technical stakeholders.

---

## 🟦ARIMA, SARIMA, and SARIMAX Models

### ARIMA (Autoregressive Integrated Moving Average)

**ARIMA** is one of the most popular classical statistical models for time series forecasting.

It is defined by three parameters **(p, d, q)**:

- **p (AR)**: Autoregressive order — number of lagged observations used.
- **d (I)**: Integrated order — number of times the series is differenced to make it stationary.
- **q (MA)**: Moving Average order — number of lagged forecast errors used.

**Best for**: Univariate time series with trend but no strong seasonality.

### SARIMA (Seasonal ARIMA)

**SARIMA** extends ARIMA to handle seasonality.

It uses six parameters: **(p, d, q)(P, D, Q)m**

- **(p, d, q)**: Non-seasonal parameters (same as ARIMA)
- **(P, D, Q)**: Seasonal parameters (same logic but for seasonal lags)
- **m**: Seasonal period (e.g., 12 for monthly data with yearly seasonality, 7 for daily with weekly seasonality)

**Best for**: Time series with both trend and clear seasonal patterns.

### SARIMAX (Seasonal ARIMA with eXogenous variables)

**SARIMAX** is SARIMA plus external (exogenous) variables.

- Allows you to include additional predictors (e.g., holidays, promotions, weather, marketing spend).
- Very powerful for real-world scenarios where external factors influence the target variable.

---

**Summary**:
- **ARIMA** → Basic model (trend only)
- **SARIMA** → Adds seasonality
- **SARIMAX** → Adds external variables

These models are widely implemented in Python via the `statsmodels` library and serve as strong baselines before moving to machine learning or deep learning approaches.

---
## 🟦Cross-Validation in Time Series Forecasting

### What is Cross-Validation in Forecasting?

**Time Series Cross-Validation** (also called **Rolling Window Cross-Validation** or **Walk-Forward Validation**) is a technique to evaluate model performance on sequential data while respecting the temporal order.

Unlike standard k-fold cross-validation used in tabular data, you **cannot** randomly shuffle time series data — doing so would cause data leakage from the future into the past.

### How Time Series Cross-Validation Works

1. **Expanding Window** (also called Rolling Origin)
   - Start with a small initial training set.
   - Train the model on the available data.
   - Forecast the next few periods (validation window).
   - Expand the training window by adding the validation data and repeat.

2. **Sliding Window** (Fixed Window)
   - Keep the training window size fixed.
   - Slide the window forward in time for each fold.

### Visual Process (Example with monthly data):

```
Training: [1 → 12]   → Validate: [13 → 15]
Training: [1 → 15]   → Validate: [16 → 18]
Training: [1 → 18]   → Validate: [19 → 21]
```

### Key Advantages:
- Provides a more realistic estimate of how the model will perform on future unseen data.
- Helps detect overfitting to specific time periods.
- Allows calculation of confidence intervals for model performance.

### Common Metrics Used:
- Average MAE, RMSE, or MAPE across all validation folds.

---

**Important Note**: Always maintain the chronological order — never use future data to predict the past.

This method is essential for reliable model selection and hyperparameter tuning in time series projects.

---

## 🟦Prophet Model by Facebook (Meta)

**Prophet** is an open-source forecasting library developed by Facebook (now Meta) designed for business time series data.

### Key Features

- Easy to use and produces high-quality forecasts with minimal tuning.
- Automatically handles **trend**, **seasonality**, and **holidays**.
- Robust to missing data and outliers.
- Works well with daily, weekly, and monthly data.

### Main Components of Prophet

Prophet decomposes the time series into:

1. **Trend** (g(t)) — Non-linear trends with automatic change point detection.
2. **Seasonality** (s(t)) — Multiple seasonalities (daily, weekly, yearly, custom).
3. **Holidays** (h(t)) — User-specified holiday effects.
4. **Error Term** (ε_t) — Remaining noise.

The model equation:
**y(t) = g(t) + s(t) + h(t) + ε_t**

### Advantages

- Very intuitive and requires little statistical expertise.
- Built-in holiday modeling (great for retail, e-commerce).
- Handles trend changes and seasonality automatically.
- Provides uncertainty intervals.
- Easy to add regressors (similar to SARIMAX).

### Limitations

- Not ideal for high-frequency data (sub-hourly).
- Less effective for very short time series.
- Can overfit if not tuned properly.

### Typical Use Case

Prophet is especially popular for **business forecasting** such as:
- Sales and demand forecasting
- Website traffic prediction
- Capacity planning

--

## 🟦Machine Learning in Time Series Forecasting

**Machine Learning (ML)** approaches treat forecasting as a supervised learning problem by creating lagged features (e.g., previous values, rolling statistics, date features).

### Common ML Models for Forecasting:
- **Tree-based models**: Random Forest, XGBoost, LightGBM, CatBoost (very popular)
- **Regression models**: Linear Regression, Ridge, Lasso
- **K-Nearest Neighbors (KNN)**
- **Support Vector Regression (SVR)**

### Strengths of ML Models:
- Handle complex non-linear relationships
- Can incorporate many external features easily
- Often outperform statistical models when lots of data and features are available
- Good at capturing interactions between variables

### Challenges:
- Need careful feature engineering (lags, rolling windows, date/time features)
- Risk of data leakage if not using proper time-series cross-validation
- Struggle with long-term forecasting without recursive strategies

---

## 🟦LSTM (Long Short-Term Memory)

**LSTM** is a type of **Recurrent Neural Network (RNN)** specifically designed to handle sequential data and long-term dependencies.

### Why LSTM?
- Traditional RNNs suffer from **vanishing gradient** problems.
- LSTM uses special **gates** (forget, input, output) to selectively remember or forget information over long periods.

### Key Advantages in Forecasting:
- Excellent at capturing complex patterns, seasonality, and long-term dependencies.
- Can model multiple seasonalities and irregular patterns.
- Works well with multivariate time series.

### Limitations:
- Requires large amounts of data.
- Computationally expensive and slower to train.
- Needs careful hyperparameter tuning and scaling.
- Often overkill for simple or small datasets.
- Harder to interpret compared to ARIMA or Prophet.

### When to Use LSTM?
- High-frequency data (minutes/hours)
- Very complex patterns with long memory
- Multivariate forecasting with many related series
- When you have sufficient historical data (thousands of observations)

**Modern Alternatives**: Transformer-based models (e.g., Temporal Fusion Transformer, Informer) are increasingly replacing LSTMs in many applications due to better performance and parallel training.
---