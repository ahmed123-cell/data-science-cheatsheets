"""
Pandas Study Reference
=====================

A runnable, section-by-section walkthrough of Pandas fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* analysis and utilities : Random sampling, outlier detection, equality checks, display options
"""

import pandas as pd
import numpy as np
from utils import ufo, drinks

#===========================================================
# Random Samples

# random_state is the seed: the same value always returns the same sample.
print(ufo.sample(n=3, random_state=42))       # n: number of rows
print(ufo.sample(frac=0.75, random_state=42).shape)  # frac: fraction of rows (75%)



#===========================================================
# Display Options

print(pd.get_option('display.max_rows'))  # 60 (default)

pd.set_option('display.max_rows', 100)    # show up to 100 rows
pd.set_option('display.max_rows', None)   # show all rows
pd.reset_option('display.max_rows')       # back to the default (60)
# The same options exist for columns (display.max_columns).

print(pd.get_option('display.max_colwidth'))  # max characters per column: 50
pd.set_option('display.max_colwidth', 70)

print(pd.get_option('display.precision'))     # decimal places shown: 6
pd.set_option('display.precision', 2)

# float_format applies to floats only; here it adds thousands separators
drinks_df = drinks.copy()
drinks_df['y'] = drinks_df['total_litres_of_pure_alcohol'] * 10000  # a large number column
pd.set_option('display.float_format', '{:,}'.format)
print(drinks_df[['total_litres_of_pure_alcohol', 'y']].head())

pd.reset_option('all')  # restore every option to its default



#===========================================================
# Checking for Equality

nan_df = pd.DataFrame({'a': [1, 2, np.nan], 'b': [1, 2, np.nan]})

# == compares element by element, and NaN never equals NaN...
print(nan_df['a'] == nan_df['b'])
# Output:
# 0     True
# 1     True
# 2    False
# dtype: bool
print(np.nan == np.nan)  # False

# ...while equals() treats NaNs in the same position as equal
print(nan_df['a'].equals(nan_df['b']))  # True



#===========================================================
# Detecting and Removing Outliers (IQR method)

# A value is an outlier if it lies more than 1.5 * IQR beyond the quartiles.
Q1 = drinks['beer_servings'].quantile(0.25)
Q3 = drinks['beer_servings'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = drinks[(drinks['beer_servings'] < lower_bound) |
                  (drinks['beer_servings'] > upper_bound)]
drinks_cleaned = drinks[(drinks['beer_servings'] >= lower_bound) &
                        (drinks['beer_servings'] <= upper_bound)]

print(outliers)
print(drinks_cleaned.shape)