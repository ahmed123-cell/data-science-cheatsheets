"""
Pandas Study Reference
=====================

A runnable, section-by-section walkthrough of Pandas fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Combining_data.py : merge(), joins, combining DataFrames and Series using concat()
"""

import pandas as pd

#===========================================================
# Merging DataFrames

# merge() joins DataFrames on matching values, like a SQL JOIN.
# With no key given, pandas joins on the column name(s) both frames share.
customers = pd.DataFrame({'ID': [1, 2, 3, 4], 'Name': ['Ali', 'Sara', 'Mohamed', 'Ahmed']})
order_totals = pd.DataFrame({'ID': [1, 2, 3, 4], 'Order': [100, 150, 200, 250]})
print(pd.merge(customers, order_totals))
# Output:
#    ID     Name  Order
# 0   1      Ali    100
# 1   2     Sara    150
# 2   3  Mohamed    200
# 3   4    Ahmed    250

# If the key columns have different names, name them with left_on / right_on
order_totals = pd.DataFrame({'Customer ID': [1, 2, 3, 4], 'Order': [100, 150, 200, 250]})
print(pd.merge(customers, order_totals, left_on='ID', right_on='Customer ID'))

# Join on the indexes of both DataFrames (only labels 1 and 2 appear in both)
customers = pd.DataFrame({'Name': ['Ali', 'Sara', 'Mohamed']}, index=[1, 2, 3])
order_totals = pd.DataFrame({'Order': [100, 150, 200]}, index=[1, 2, 4])
print(pd.merge(customers, order_totals, left_index=True, right_index=True))
# Output:
#    Name  Order
# 1   Ali    100
# 2  Sara    150

# Join the index of one DataFrame with a column of the other
order_totals = pd.DataFrame({'ID': [1, 2, 4], 'Order': [100, 150, 200]})
print(pd.merge(customers, order_totals, left_index=True, right_on='ID', how='outer'))

# Join types (how=...)
left = pd.DataFrame({'color': ['green', 'yellow', 'red'], 'num': [1, 2, 3]})
right = pd.DataFrame({'color': ['green', 'yellow', 'pink'], 'size': ['S', 'M', 'L']})

print(pd.merge(left, right, how='inner'))  # only keys present in BOTH (default)
# Output:
#     color  num size
# 0   green    1    S
# 1  yellow    2    M
print(pd.merge(left, right, how='outer'))  # keys from EITHER; gaps become NaN
# Output:
#     color  num size
# 0   green  1.0    S
# 1    pink  NaN    L
# 2     red  3.0  NaN
# 3  yellow  2.0    M
print(pd.merge(left, right, how='left'))   # every key of the left DataFrame
# Output:
#     color  num size
# 0   green    1    S
# 1  yellow    2    M
# 2     red    3  NaN
print(pd.merge(left, right, how='right'))  # every key of the right DataFrame
# Output:
#     color  num size
# 0   green  1.0    S
# 1  yellow  2.0    M
# 2    pink  NaN    L