"""
Pandas Study Reference
=====================

A runnable, section-by-section walkthrough of Pandas fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Grouping and Aggregation  : groupby(), aggregation, transform(), value_counts(), crosstab(), correlation
"""

import pandas as pd
from utils import drinks, orders, movies


#===========================================================
# Groupby: Analysing Data by Category

# Aggregate one column per continent
print(drinks.groupby('continent')['beer_servings'].mean())
print(drinks.groupby('continent')['beer_servings'].agg(['count', 'min', 'max', 'mean']))

# Mean of every numeric column per continent
print(drinks.groupby('continent').mean(numeric_only=True))

# Extract the rows of a single group
print(drinks.groupby('continent').get_group('Africa').head())

# Summary statistics per group
print(drinks.groupby('continent')['wine_servings'].describe())

# Keep only groups that satisfy a condition (here: every continent except Africa)
non_african = drinks.groupby('continent').filter(lambda group: group.name != 'Africa')
print(non_african['wine_servings'].value_counts().head())



#===========================================================
# Aggregation: groupby().sum() vs transform()

orders_df = orders.copy()

# item_price is text ("$2.39"), so convert it to float first. Without this,
# sum() would concatenate the strings instead of adding the numbers.
orders_df['item_price'] = orders_df['item_price'].str.replace('$', '', regex=False).astype(float)

# sum() returns ONE row per group (one per order)
print(orders_df.groupby('order_id')['item_price'].sum().head())

# transform() returns a result the SAME LENGTH as the original (4622 rows),
# repeating each group's total on every row of that group.
total_price = orders_df.groupby('order_id')['item_price'].transform('sum')
orders_df['total_price'] = total_price
orders_df['percent_of_total'] = orders_df['item_price'] / orders_df['total_price']
print(orders_df.head())



#===========================================================
# Exploring a Series

print(movies['genre'].value_counts())                      # count of each category
print(movies['genre'].value_counts(normalize=True) * 100)  # proportions, as percentages

print(movies['genre'].unique())   # array of the distinct values
print(movies['genre'].nunique())  # number of distinct values

# crosstab() counts how often each pair of categories occurs together.
# Parameters: index, columns, values, margins, aggfunc, normalize
print(pd.crosstab(movies['genre'], movies['content_rating']))



#===========================================================
# Correlation

# Correlation between two columns (-1 to 1)
print(drinks['beer_servings'].corr(drinks['total_litres_of_pure_alcohol']))

# Correlation matrix of all numeric columns
print(drinks.corr(numeric_only=True))