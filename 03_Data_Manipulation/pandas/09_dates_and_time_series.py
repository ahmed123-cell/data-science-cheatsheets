"""
Pandas Study Reference
=====================

A runnable, section-by-section walkthrough of Pandas fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Dates and times    : Datetime conversion, date components, date ranges,
                        resample(), rolling(), shift(), diff(), pct_change(), expanding(), interpolation
"""

import pandas as pd
import numpy as np
from utils import ufo, drinks

#===========================================================
# Dates and Times

ufo_df = ufo.copy()

# to_datetime(data, format): convert text to the datetime type
ufo_df['Time'] = pd.to_datetime(ufo_df['Time'])
print(ufo_df.dtypes)

# The .dt accessor exposes date/time components
print(ufo_df['Time'].dt.hour.head())          # hour of the day
print(ufo_df['Time'].dt.day_name().head())    # name of the weekday
print(ufo_df['Time'].dt.day_of_year.head())   # day of the year (1-366)
print(ufo_df['Time'].dt.weekday.head())       # weekday number (Monday = 0)
print(ufo_df['Time'].dt.is_leap_year.head())  # leap-year flag

# Convert to a period (Y, M, Q, D) and back to a timestamp
ufo_df['month'] = ufo_df['Time'].dt.to_period('M')
ufo_df['month'] = ufo_df['month'].dt.to_timestamp(how='start')
print(ufo_df['month'].head())

# Format dates as text. The result is a string column, so it is NOT stored
# back in 'Time' (that would break the date comparisons below).
print(ufo_df['Time'].dt.strftime('%d/%m/%Y').head())

# Filter by date
timestamp = pd.to_datetime('1/1/1999')
print(ufo_df.loc[ufo_df['Time'] >= timestamp, :].head())

# Subtracting datetimes gives a Timedelta
print((ufo_df['Time'].max() - ufo_df['Time'].min()).days)

# Build datetimes from columns named year / month / day (and optionally hour...)
date_parts = pd.DataFrame([[12, 25, 2017, 10], [1, 15, 2018, 11]],
                          columns=['month', 'day', 'year', 'hour'])
print(pd.to_datetime(date_parts))                           # from the whole DataFrame
# Output:
# 0   2017-12-25 10:00:00
# 1   2018-01-15 11:00:00
# dtype: datetime64[us]
print(pd.to_datetime(date_parts[['month', 'day', 'year']])) # from a subset of columns

# Use the new datetimes as the index
date_parts.index = pd.to_datetime(date_parts[['month', 'day', 'year']])
print(date_parts)

# Generate a sequence of dates. Give three of: start, end, periods, freq.
# ('ME' = month end;)
dates = pd.date_range(start='2023-01-01', periods=6, freq='ME')
print(dates)
# Output: DatetimeIndex(['2023-01-31', '2023-02-28', ..., '2023-06-30'], freq='ME')



#===========================================================
# Filling Gaps with interpolate()

# interpolate(method, axis, inplace) estimates missing values from their neighbours.
# Common methods: linear, polynomial, spline, bfill, ffill, time, index, nearest
gaps = pd.DataFrame({'A': [57.4, 24.9, np.nan, 329.2, 23.10]})
print(gaps.interpolate(method='linear'))
# Output (the NaN becomes the midpoint of 24.9 and 329.2):
#         A
# 0   57.40
# 1   24.90
# 2  177.05
# 3  329.20
# 4   23.10



#===========================================================
# Time Series: resample, rolling, shift

# Build one row per day per city for two years
dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
locations = ['Cairo', 'Alexandria', 'Mansoura']
daily = pd.DataFrame([(date, loc) for date in dates for loc in locations],
                     columns=['Date', 'Location'])

# Simulated spending: a yearly seasonal wave plus random noise (seeded for repeatability)
np.random.seed(42)
daily['Total Spent'] = (
    100 + 20 * np.sin(daily['Date'].dt.dayofyear * 2 * np.pi / 365)
    + np.random.normal(loc=0, scale=10, size=len(daily))
).round(2)

# A DatetimeIndex unlocks resample(), rolling() and friends
daily.set_index('Date', inplace=True)

# resample(rule): group by time period, then aggregate ('ME' = month end)
print(daily['Total Spent'].resample('ME').mean())

# rolling(window, min_periods): moving average over the last 7 rows
# (the first 6 values are NaN because the window is not yet full)
print(daily['Total Spent'].rolling(window=7).mean().head(10))

# shift(periods, fill_value, freq): move values down, e.g. to compare with the previous row
print(daily['Total Spent'].shift(periods=1).head())



#===========================================================
# diff, pct_change and expanding

print(drinks['beer_servings'].diff().head())        # difference from the previous row
print(drinks['beer_servings'].pct_change().head())  # same as diff, as a fraction of the previous value
print(drinks['beer_servings'].expanding().sum().head())  # cumulative sum from the first row