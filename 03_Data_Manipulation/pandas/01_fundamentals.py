"""
Pandas Study Reference
=====================

A runnable, section-by-section walkthrough of Pandas fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Basics    : Creating Series, DataFrames, reading data, common methods and attributes
"""

import pandas as pd
import numpy as np
from utils import movies, ORDERS_URL, USERS_URL

# Column names of the movie-users file (it has no header row)
USER_COLS = ['user_id', 'age', 'gender', 'occupation', 'zip_code']

#===========================================================
# Creating a Series

# A Series is a one-dimensional labelled array.
data = [1, 7, 2]
series = pd.Series(data)
print(series)
# Output:
# 0    1
# 1    7
# 2    2
# dtype: int64
print(series[0])  # 1 -> access by label (the default index is 0, 1, 2, ...)

# Custom index labels
series_labeled = pd.Series(data, index=['x', 'y', 'z'])
print(series_labeled['y'])  # 7

# From a dictionary: keys become the index. Passing `index` selects/orders keys.
calories = {"day1": 420, "day2": 380, "day3": 390}
selected_days = pd.Series(calories, index=["day1", "day2"])
print(selected_days)
# Output:
# day1    420
# day2    380
# dtype: int64



#===========================================================
# Creating a DataFrame

# A DataFrame is a two-dimensional table: a collection of Series sharing an index.
data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}
df = pd.DataFrame(data)
print(df)
# Output:
#    calories  duration
# 0       420        50
# 1       380        40
# 2       390        45

# Named index and an explicit column order
df = pd.DataFrame(data, index=["day1", "day2", "day3"], columns=['duration', 'calories'])
print(df)
# Output:
#       duration  calories
# day1        50       420
# day2        40       380
# day3        45       390
print(df.loc['day1'])  # one row, returned as a Series
# Output:
# duration     50
# calories    420
# Name: day1, dtype: int64

# From a list of lists
print(pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'red']], columns=['id', 'color']))
# Output:
#     id color
# 0  100   red
# 1  101  blue
# 2  102   red

# From a numpy array (values are random, so they change on every run)
arr = np.random.randint(1, 50, size=(4, 2))
print(pd.DataFrame(arr, columns=['one', 'two']))

# Random test scores, using the student ID as the index
student_scores = pd.DataFrame({
    'student': np.arange(100, 110),
    'test scores': np.random.randint(30, 100, size=10),
}).set_index('student')
print(student_scores)

# Combine a DataFrame and a Series with concat (axis=1 -> side by side).
# Rows are aligned by index label; missing labels become NaN.
df = pd.DataFrame({'id': [100, 101, 102], 'color': ['red', 'blue', 'red']},
                  columns=['color', 'id'], index=['a', 'b', 'c'])
shape = pd.Series(['round', 'square'], index=['c', 'b'], name='shape')
print(pd.concat([df, shape], axis=1))
# Output:
#   color   id   shape
# a   red  100     NaN
# b  blue  101  square
# c   red  102   round



#===========================================================
# Reading Data with read_table()

# read_table() is read_csv() with a tab as the default separator.
print(pd.read_table(ORDERS_URL).head())

# Common parameters:
#   path, sep, header, names, index_col, usecols, dtype, skiprows, nrows,
#   na_values, encoding, parse_dates, skipfooter, engine

# Customise the read: pipe separator, no header row, custom names,
# only two columns, and only the first 10 rows.
users_sample = pd.read_table(USERS_URL, sep='|', header=None, names=USER_COLS,
                             usecols=['user_id', 'occupation'], nrows=10)
print(users_sample.head())



#===========================================================
# Common Methods and Attributes

print(movies.head())  # first 5 rows
print(movies.tail())  # last 5 rows

print(movies.describe())               # summary statistics of numeric columns
print(movies.describe(include='all'))  # summary of every column
movies.info()                          # column types, non-null counts, memory use

print(movies.shape)    # (rows, columns) -> (979, 6)
print(movies.dtypes)   # data type of every column
print(movies.columns)  # column names
print(movies.index)    # RangeIndex(start=0, stop=979, step=1)