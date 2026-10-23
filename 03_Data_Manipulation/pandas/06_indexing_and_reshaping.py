"""
Pandas Study Reference
=====================

A runnable, section-by-section walkthrough of Pandas fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Indexing and Reshaping : Working with indexes, Series alignment, multi-level indexes, unstack(), pivot_table(), melt()
"""

import pandas as pd
import numpy as np
from utils import drinks, DRINKS_URL, stocks, STOCKS_URL, titanic


#===========================================================
# Working with the Index

drinks_df = drinks.copy()

# Use a column as the row index
drinks_df.set_index('country', inplace=True)
print(drinks_df.head())

# ...or set the index while reading the file
drinks_df = pd.read_csv(DRINKS_URL, index_col='country')

# The index has a name, shown above the index labels. It can be removed or changed.
drinks_df.index.name = None
print(drinks_df.head())

# Turn the index back into a regular column
drinks_df.index.name = "Country"
drinks_df.reset_index("Country", inplace=True)
print(drinks_df.head())

# --- Index of a Series ---
drinks_by_country = drinks.set_index('country')
continent_counts = drinks_by_country['continent'].value_counts()

print(continent_counts.index)             # the labels
print(continent_counts.values)            # the counts, as a numpy array
print(continent_counts.sort_values())     # sort by values
print(continent_counts.sort_index())      # sort by index labels

# Operations between Series align on the index (broadcasting by label).
# Countries missing from `people` become NaN.
people = pd.Series([3000000, 85000], index=['Albania', 'Andorra'],
                   name='population', dtype=np.int32)
print((drinks_by_country['beer_servings'] * people).head())

# Add the Series as a new column with concat
print(pd.concat([drinks_by_country, people], axis=1).head())



#===========================================================
# Expanding a Series of Lists into Columns

lists_df = pd.DataFrame({'col one': ['a', 'b', 'c'],
                         'col two': [[10, 40], [20, 50], [30, 60]]})

# apply(pd.Series) turns each list into a row of columns
expanded = lists_df['col two'].apply(pd.Series)
print(pd.concat([lists_df, expanded], axis=1))
# Output:
#   col one   col two   0   1
# 0       a  [10, 40]  10  40
# 1       b  [20, 50]  20  50
# 2       c  [30, 60]  30  60



#===========================================================
# Multi-Level Index

stocks_df = stocks.copy()

# Grouping by two columns produces a Series with a two-level index
ser = stocks_df.groupby(['Symbol', 'Date'])['Close'].mean()
print(ser)
print(ser.index)
print(ser.unstack())  # move the inner level into columns -> DataFrame

# pivot_table() gives the same table directly
pivot = stocks_df.pivot_table(values='Close', index='Symbol', columns='Date')
print(pivot)

# Select from the multi-index Series
print(ser.loc['AAPL', '2016-10-03'])
print(ser.loc[:, '2016-10-03'])  # ':' = all values of the first level

# Convert the columns into a multi-level index (sorted for faster lookups)
stocks_df.set_index(['Symbol', 'Date'], inplace=True)
stocks_df.sort_index(inplace=True)
print(stocks_df)

# Swap the index levels
print(stocks_df.groupby(['Date', 'Symbol'])['Close'].sum().swaplevel().sort_index())

# Select from the multi-index DataFrame
print(stocks_df.loc['AAPL'])                                # outer level only
print(stocks_df.loc['AAPL', '2016-10-03'])                  # both levels
print(stocks_df.loc['AAPL', '2016-10-03']['Close'])         # then pick a column
print(stocks_df.loc[('AAPL', '2016-10-03'), :])             # tuple = explicit (row key, columns)
print(stocks_df.loc[('AAPL', '2016-10-03'), 'Close'])
print(stocks_df.loc[(['AAPL', 'MSFT'], '2016-10-03'), :])   # several outer values
print(stocks_df.loc[(slice(None), ['2016-10-03', '2016-10-04']), :])  # slice(None) = all outer values

# Merge two objects on their (multi-level) indexes
close = stocks_df.loc[:, 'Close']
volume = pd.read_csv(STOCKS_URL, usecols=[0, 2, 3], index_col=['Symbol', 'Date'])
print(pd.merge(close, volume, left_index=True, right_index=True))



#===========================================================
# Reshaping: unstack and pivot_table

# Mean survival rate by sex and passenger class
print(titanic.groupby(['Sex', 'Pclass'])['Survived'].mean().unstack())

# pivot_table() does the same in one step
print(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived', aggfunc='mean'))

# margins=True adds an "All" row and column with the overall result
print(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived',
                          aggfunc='mean', margins=True))
print(titanic.pivot_table(index='Sex', columns='Pclass', values='Survived',
                          aggfunc='count', margins=True))



#===========================================================
# Unpivoting with melt()

# melt() converts wide data (one column per subject) into long data
# (one row per student-subject pair).
# Parameters: id_vars, value_vars, var_name, value_name
scores = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Math': [85, 90], 'Science': [88, 92]})
print(pd.melt(scores, id_vars=['Name'], var_name='Subject', value_name='Score'))
# Output:
#     Name  Subject  Score
# 0  Alice     Math     85
# 1    Bob     Math     90
# 2  Alice  Science     88
# 3    Bob  Science     92