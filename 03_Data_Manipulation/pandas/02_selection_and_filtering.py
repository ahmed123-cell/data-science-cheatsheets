"""
Pandas Study Reference
=====================

A runnable, section-by-section walkthrough of Pandas fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* selection & Sorting : Selecting columns, creating columns, loc, iloc, filtering, multiple conditions, sorting, dropping rows/columns
"""

import pandas as pd
from utils import ufo, movies

#===========================================================
# Selecting a Series and Creating New Columns

ufo_df = ufo.copy()

print(ufo_df['City'].head())  # select one column -> Series

# Create a new column by combining two string columns
ufo_df['location'] = ufo_df['City'] + ', ' + ufo_df['State']
print(ufo_df.head())



#===========================================================
# Selecting with loc and iloc

ufo_df = ufo.copy()

# loc selects by LABEL. The end of a slice is INCLUDED.
print(ufo_df.loc[0])                               # one row
print(ufo_df.loc[0:2])                             # rows 0, 1 and 2
print(ufo_df.loc[:, ['City', 'State']].head())     # chosen columns
print(ufo_df.loc[0:2, 'City':'State'])             # rows and a range of columns
print(ufo_df.loc[ufo_df['City'] == 'Oakland']['State'].head())  # boolean filter

# iloc selects by integer POSITION. The end of a slice is EXCLUDED.
print(ufo_df.iloc[:, 0:2].head())                  # first two columns
print(ufo_df.iloc[0:3, :])                         # first three rows
print(ufo_df.iloc[0:3, [0, 3]])                    # rows 0-2, columns 0 and 3



#===========================================================
# Removing Columns and Rows

ufo_df = ufo.copy()

# axis=1 -> columns, axis=0 -> rows
ufo_df.drop('Colors Reported', axis=1, inplace=True)  # one column
print(ufo_df.head())

ufo_df.drop(['City', 'State'], axis=1, inplace=True)  # several columns
print(ufo_df.head())

ufo_df.drop([0, 1], axis=0, inplace=True)             # rows, by index label
print(ufo_df.head())



#===========================================================
# Sorting

# Sort a Series
print(movies['title'].sort_values().head())                 # ascending (default)
print(movies['title'].sort_values(ascending=False).head())  # descending

# Sort a DataFrame by one column
print(movies.sort_values('title').head())

# Sort by several columns (ties in the first column are broken by the next)
print(movies.sort_values(['content_rating', 'duration']).head())



#===========================================================
# Filtering Rows by Column Value

# A comparison produces a boolean Series (True = keep the row)
long_movies = movies['duration'] >= 200
print(long_movies.head())

# Use the boolean Series to filter the DataFrame
crime_movies = movies[movies['genre'] == 'Crime']
print(crime_movies.head())

# Select a single column of the filtered result
print(movies[movies['genre'] == 'Crime']['genre'].head())
print(movies.loc[movies['genre'] == 'Crime', 'genre'].head())  # preferred: one step, more efficient



#===========================================================
# Multiple Filter Conditions

# Wrap each condition in parentheses and combine with & (and), | (or), ~ (not)
print(movies[(movies['duration'] >= 200) & (movies['genre'] == 'Drama')].head())
print(movies[(movies['duration'] >= 200) | (movies['genre'] == 'Drama')].head())
print(movies[(movies['duration'] >= 200) & ~(movies['genre'] == 'Drama')].head())

# isin() is a shorter way to match several categories; ~ negates it
print(movies[movies['genre'].isin(['Crime', 'Drama', 'Action'])].head())
print(movies[~movies['genre'].isin(['Action', 'Drama', 'Western'])].head())

# Filter by the N most frequent categories
genre_counts = movies['genre'].value_counts()
print(genre_counts.nlargest(3))
print(movies[movies['genre'].isin(genre_counts.nlargest(3).index)].head())