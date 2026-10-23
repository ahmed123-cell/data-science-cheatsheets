"""
Pandas Study Reference
=====================

A runnable, section-by-section walkthrough of Pandas fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Dataframe Operations : String methods, map(), apply(), iterating over DataFrames, axis, selecting columns by data type
"""

import pandas as pd
import numpy as np
from utils import orders, titanic, drinks, ufo


#===========================================================
# String Methods

# The .str accessor applies string methods to a whole Series.
print(orders['item_name'].str.contains('Chicken').head())  # boolean Series
print(orders[orders['item_name'].str.contains('Chicken')].head())  # use it to filter

print(orders['item_name'].str.upper().head())

# Chain methods to clean text. regex=False treats '[' and ']' as plain characters.
print(orders['choice_description'].str.replace('[', '', regex=False)
                                  .str.replace(']', '', regex=False).head())

# See the pandas API reference ("Series.str") for more string methods.



#===========================================================
# Applying Functions: map() and apply()

titanic_df = titanic.copy()
drinks_df = drinks.copy()

# --- map(): element-wise on a Series (a dictionary or a simple function) ---
titanic_df['Sex_num'] = titanic_df['Sex'].map({'female': 0, 'male': 1})  # dictionary
print(titanic_df.loc[0:4, ['Sex', 'Sex_num']])

titanic_df['Age plus 30'] = titanic_df['Age'].map(lambda x: x + 30)      # function
print(titanic_df.loc[0:4, ['Age', 'Age plus 30']])

# On a DataFrame, map() applies a function to every cell
print(drinks_df.loc[:, 'beer_servings':'wine_servings'].map(float).head())

# --- apply(): more flexible; works on a Series or along a DataFrame axis ---
titanic_df['Name_length'] = titanic_df['Name'].apply(len)                # built-in function
print(titanic_df.loc[0:4, ['Name', 'Name_length']])

titanic_df['Fare_ceil'] = titanic_df['Fare'].apply(np.ceil).astype(np.int16)  # numpy function
print(titanic_df.loc[0:4, ['Fare', 'Fare_ceil']])


def get_element(items, position):
    """Return the element at `position` from a list-like value."""
    return items[position]


# Extra arguments are passed through apply() as keyword arguments
last_names = titanic_df['Name'].str.split(',').apply(get_element, position=0)
print(last_names.head())

# The same result with a lambda
print(titanic_df['Name'].str.split(',').apply(lambda parts: parts[0]).head())

# On a DataFrame: axis=0 -> once per column, axis=1 -> once per row
servings = drinks_df.loc[:, 'beer_servings':'wine_servings']
print(servings.apply(max, axis=0))
print(servings.apply(max, axis=1).head())

# Row-wise apply with a custom function: family size = siblings/spouses + parents/children + the passenger
titanic_df['family_size'] = titanic_df.apply(
    lambda row: row['SibSp'] + row['Parch'] + 1, axis=1)
print(titanic_df[['SibSp', 'Parch', 'family_size']].head())



#===========================================================
# The "axis" Parameter

# axis=0 -> operate down the rows (one result per column)
# axis=1 -> operate across the columns (one result per row)
print(drinks.mean(numeric_only=True, axis=0))        # mean of every column
print(drinks.mean(numeric_only=True, axis=1).head()) # mean of every row

# The same idea works for other methods such as std() or sum().



#===========================================================
# Iterating Over a DataFrame

# Only the first 5 rows are printed here to keep the output short.

# iterrows(): yields (index, row-as-Series) -- convenient but slow
for index, row in ufo.head().iterrows():
    print(index, row['City'], row['State'])

# itertuples(): yields named tuples -- faster than iterrows
for row in ufo.head().itertuples():
    print(row.City)



#===========================================================
# Selecting Columns by Data Type

print(drinks.select_dtypes(include='number').head())    # numeric columns
print(drinks.select_dtypes(include=['object', 'string']).head())  # text columns
print(drinks.select_dtypes(include=['number', 'object', 'string', 'category', 'datetime']).head())
print(drinks.select_dtypes(exclude='number').head())    # everything except numeric