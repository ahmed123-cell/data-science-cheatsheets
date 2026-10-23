"""
Pandas Study Reference
=====================

A runnable, section-by-section walkthrough of Pandas fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Data Cleaning : Renaming columns, changing data types, replacing values, missing values,
                  duplicate rows, safe string-to-number conversion
"""

import pandas as pd
import numpy as np
from utils import ufo, orders, drinks, movies, UFO_URL, DRINKS_URL, USERS_URL

# Column names of the movie-users file (it has no header row)
USER_COLS = ['user_id', 'age', 'gender', 'occupation', 'zip_code']


#===========================================================
# Renaming Columns

ufo_df = ufo.copy()

# Method 1: rename() with a dictionary (only the listed columns change)
ufo_df.rename(columns={'Colors Reported': 'Colors', 'Shape Reported': 'Shape'}, inplace=True)
print(ufo_df.columns)

# Method 2: replace all column names at once (the list must match the column count)
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo_df.columns = ufo_cols
print(ufo_df.columns)

# Method 3: rename while reading. header=0 tells pandas the file already has
# a header row, which `names` then replaces.
ufo_df = pd.read_csv(UFO_URL, names=ufo_cols, header=0)
print(ufo_df.head())

# Method 4: string methods on the column names
ufo_df.columns = ufo_df.columns.str.replace(" ", "_")
print(ufo_df.columns)
# Output: Index(['city', 'colors_reported', 'shape_reported', 'state', 'time'], dtype=...)

# Add a prefix or suffix to every column name (returns a new DataFrame)
df = pd.DataFrame({'col one': [100, 200], 'col two': [300, 400]})
print(df.add_prefix('X_'))
# Output:
#    X_col one  X_col two
# 0        100        300
# 1        200        400
print(df.add_suffix('_Y'))
# Output:
#    col one_Y  col two_Y
# 0        100        300
# 1        200        400



#===========================================================
# Changing Data Types

orders_df = orders.copy()

# Remove "$" and convert text to float
prices = orders_df['item_price'].str.replace('$', '', regex=False).astype(float)
print(prices.head())

# Boolean -> int (True = 1, False = 0)
print(orders_df['item_name'].str.contains('Chicken').astype(int).head())

# Set the type while reading the file
drinks_df = pd.read_csv(DRINKS_URL, dtype={'beer_servings': float})
print(drinks_df.dtypes)

# Convert several columns at once
drinks_df = drinks.astype({'beer_servings': float, 'spirit_servings': float})
print(drinks_df.dtypes)



#===========================================================
# Replacing Values

movies_df = movies.copy()

# Replace a value using a boolean filter: 'NOT RATED' -> NaN
movies_df.loc[movies_df['content_rating'] == 'NOT RATED', 'content_rating'] = np.nan

# Change a single value. .copy() avoids pandas' SettingWithCopy warning when
# editing a filtered DataFrame.
top_movies = movies.loc[movies['star_rating'] >= 9, :].copy()
top_movies.loc[0, 'duration'] = 150
print(top_movies.head())

# replace() swaps several values at once across the whole DataFrame
print(movies.replace(['UNRATED', 'NOT RATED'], np.nan).head())



#===========================================================
# Handling Missing Values

ufo_df = ufo.copy()

# Detect missing values
print(ufo_df.isnull().tail())   # True where a value is missing
print(ufo_df.notnull().tail())  # the opposite
print(ufo_df.isnull().sum())    # number of missing values per column

# Drop rows. how='any' drops a row if ANY value is missing,
# how='all' only if ALL values are missing, subset limits which columns are checked.
print(ufo_df.dropna(how='any').shape)
print(ufo_df.dropna(how='all').shape)
print(ufo_df.dropna(subset=['City', 'Shape Reported'], how='any').shape)

# Drop columns instead of rows
print(ufo_df.dropna(axis=1).head())  # drop every column that contains a missing value
# thresh = minimum number of non-missing values required to keep a column,
# so this drops columns with more than 10% missing values.
print(ufo_df.dropna(thresh=len(ufo_df) * 0.9, axis=1).head())

# Count values, including missing ones
print(ufo_df['Shape Reported'].value_counts(dropna=False).head())

# Fill missing values. Assigning the result back is the recommended pattern
# (calling fillna(inplace=True) on a single column is unreliable in newer pandas).
ufo_df['Shape Reported'] = ufo_df['Shape Reported'].fillna('Unknown')
print(ufo_df['Shape Reported'].value_counts().head())



#===========================================================
# Removing Duplicate Rows

users = pd.read_table(USERS_URL, sep='|', header=None, names=USER_COLS,
                      index_col='user_id')

print(users['zip_code'].duplicated().sum())  # duplicates in one column
print(users.duplicated().sum())              # fully duplicated rows

# duplicated(keep=...) decides which copy is NOT flagged as a duplicate
print(users.loc[users.duplicated(keep='first'), :])  # flags later copies, keeps the first
print(users.loc[users.duplicated(keep='last'), :])   # flags earlier copies, keeps the last
print(users.loc[users.duplicated(keep=False), :])    # flags every copy

# drop_duplicates(subset, keep, ignore_index, inplace)
print(users.drop_duplicates(keep='first').shape)

# Consider only some columns when deciding what counts as a duplicate
print(users.duplicated(subset=['age', 'zip_code']).sum())
print(users.drop_duplicates(subset=['age', 'zip_code']).shape)



#===========================================================
# Converting Strings to Numbers Safely

text_numbers = pd.DataFrame({'col one': ['1.1', '2.2', '3.3'],
                             'col two': ['4.4', '5.5', '6.6'],
                             'col three': ['7.7', '8.8', '-']})

# astype() works only when every value is convertible
print(text_numbers.astype({'col one': float, 'col two': float}).dtypes)

# to_numeric(errors='coerce') turns invalid values (like '-') into NaN,
# which can then be filled.
print(pd.to_numeric(text_numbers['col three'], errors='coerce').fillna(0))
# Output:
# 0    7.7
# 1    8.8
# 2    0.0
# Name: col three, dtype: float64