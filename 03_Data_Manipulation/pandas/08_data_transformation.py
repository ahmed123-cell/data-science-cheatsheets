"""
Pandas Study Reference
=====================

A runnable, section-by-section walkthrough of Pandas fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Data Transformation : Dummy variables, categorical data, splitting strings,
                        expanding lists into columns, explode(), binning with cut() and qcut()
"""

import ast
import pandas as pd
from utils import titanic, drinks, movies, DRINKS_URL

#===========================================================
# Dummy Variables (useful for machine learning)

titanic_df = titanic.copy()

# Method 1: map() with a dictionary (for a column with two values)
titanic_df['Sex_male'] = titanic_df['Sex'].map({'female': 0, 'male': 1})
print(titanic_df[['Sex', 'Sex_male']].head())

# Method 2: get_dummies() on one column, dropping the first dummy column
# (iloc[:, 1:]) because it is redundant: if all others are 0, it must be the first.
embarked_dummies = pd.get_dummies(titanic_df['Embarked'], prefix='Embarked',
                                  prefix_sep='-').iloc[:, 1:]
print(pd.concat([titanic_df, embarked_dummies], axis=1).head())

# Method 3 (most flexible): get_dummies() on the whole DataFrame
print(pd.get_dummies(titanic_df, columns=['Sex', 'Embarked'], drop_first=True).head())



#===========================================================
# The "category" Data Type

# category is a pandas type for categorical variables, e.g. (male, female) or
# (small, medium, big).
#
# * Memory/performance: pandas stores each unique value once and keeps a column
#   of integer codes, which is far smaller than repeating strings. Use it for
#   string columns with few unique values.
# * Ordering: categories can have a logical order, e.g. small < medium < big.

drinks_df = drinks.copy()
drinks_df.info(memory_usage='deep')  # before converting

drinks_df['continent'] = drinks_df['continent'].astype('category')
print(drinks_df.dtypes)                      # 'continent' is now category

print(drinks_df['continent'].cat.codes.head())  # the integer codes
print(drinks_df['continent'].cat.categories)    # the unique values the codes refer to
print(drinks_df.memory_usage(deep=True))        # 'continent' now uses far less memory

# Ordered categories
quality_df = pd.DataFrame({'ID': [100, 101, 102, 103],
                           'quality': ['good', 'very good', 'good', 'excellent']})
quality_df['quality'] = pd.Categorical(quality_df['quality'],
                                       categories=['good', 'very good', 'excellent'],
                                       ordered=True)
print(quality_df.sort_values('quality'))  # sorts by the defined order, not alphabetically
# Output:
#     ID    quality
# 0  100       good
# 2  102       good
# 1  101  very good
# 3  103  excellent
print(quality_df.loc[quality_df['quality'] > 'good'])  # comparisons respect the order
# Output:
#     ID    quality
# 1  101  very good
# 3  103  excellent

# Set the type while reading the file
drinks_df = pd.read_csv(DRINKS_URL, dtype={'continent': 'category'})
print(drinks_df.dtypes)



#===========================================================
# Splitting a String into Columns

people_df = pd.DataFrame({'name': ['John Arther Doe', 'Jane Ann Smith'],
                          'location': ['Los Angelose, CA', 'Washington, DC']})

# expand=True returns a DataFrame with one column per piece
people_df[['first', 'middle', 'last']] = people_df['name'].str.split(' ', expand=True)
print(people_df)
# Output:
#               name          location first  middle   last
# 0  John Arther Doe  Los Angelose, CA  John  Arther    Doe
# 1   Jane Ann Smith    Washington, DC  Jane     Ann  Smith



#===========================================================
# Exploding Lists into Rows

movies_df = movies.copy()

# actors_list is stored as TEXT that looks like a list. literal_eval() safely
# converts it into a real list (prefer it over eval(), which can run arbitrary code).
movies_df['actors_list'] = movies_df['actors_list'].apply(ast.literal_eval)

# explode() creates one row per list element, repeating the other columns
print(movies_df.explode('actors_list').head())



#===========================================================
# Binning: cut() vs qcut()

# cut():  bins of EQUAL WIDTH (each covers the same range of values)
# qcut(): bins with an EQUAL NUMBER OF ELEMENTS (quantiles)
values = pd.Series([1, 10, 20, 30, 40, 50])

print(pd.cut(values, bins=3))
# Output:
# 0     (0.951, 17.333]
# 1     (0.951, 17.333]
# 2    (17.333, 33.667]
# 3    (17.333, 33.667]
# 4      (33.667, 50.0]
# 5      (33.667, 50.0]
# dtype: category
print(pd.qcut(values, q=3, labels=['Low', 'Medium', 'High']))
# Output:
# 0       Low
# 1       Low
# 2    Medium
# 3    Medium
# 4      High
# 5      High
# dtype: category