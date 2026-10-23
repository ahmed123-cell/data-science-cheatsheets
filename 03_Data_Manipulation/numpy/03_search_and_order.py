"""
NumPy Study Reference
=====================

A runnable, section-by-section walkthrough of NumPy fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Search & order  : where, searchsorted, sort, argsort, boolean filtering
"""

import numpy as np

#========================
# Searching Arrays

# where(condition) returns the indexes where the condition is True.
# The result is a tuple with one index array per dimension.
arr = np.array([1, 2, 3, 4, 5, 4, 4])
print(np.where(arr == 4))      # --> (array([3, 5, 6]),)
print(np.where(arr % 2 == 0))  # --> (array([1, 3, 5, 6]),)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.where(arr == 4))      # --> (array([0]), array([3]))                  (rows, columns)
print(np.where(arr % 2 == 0))  # --> (array([0, 0, 1, 1]), array([1, 3, 1, 3]))

# where(condition, x, y) replaces elements: x where True, y where False
arr = np.array([[1, 2, 3], [4, 5, 6]])
replaced = np.where(arr < 4, 0, arr)
print(replaced)
# --> [[0 0 0]
#      [4 5 6]]

# searchsorted does a binary search on a SORTED array and returns the index
# where the value would be inserted to keep the order
arr = np.array([6, 7, 8, 9])
print(np.searchsorted(arr, 7))                # --> 1  (leftmost valid position)
print(np.searchsorted(arr, 7, side='right'))  # --> 2  (rightmost valid position)

# Search for several values at once
arr = np.array([1, 3, 5, 7, 9])
print(np.searchsorted(arr, [2, 4, 6]))  # --> [1 2 3]


#========================
# Sorting Arrays

# sort returns a sorted copy (numbers, strings, and booleans all work)
print(np.sort(np.array([3, 2, 0, 1])))                     # --> [0 1 2 3]
print(np.sort(np.array(['banana', 'apple', 'orange'])))    # --> ['apple' 'banana' 'orange']
print(np.sort(np.array([True, False, True])))              # --> [False  True  True]

# 2D arrays are sorted along the last axis (each row) by default
arr_2d = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr_2d))
# --> [[2 3 4]
#      [0 1 5]]

# axis=0 sorts down each column
print(np.sort(arr_2d, axis=0))
# --> [[3 0 1]
#      [5 2 4]]

# argsort returns the indexes that would sort the array
arr = np.array([3, 1, 4, 2])
print(np.argsort(arr))  # --> [1 3 0 2]

# Use argsort to reorder whole rows by the values in the first column
arr_2d = np.array([[9, 3, 1], [7, 4, 2], [0, 5, 3]])
print(arr_2d[arr_2d[:, 0].argsort()])
# --> [[0 5 3]
#      [7 4 2]
#      [9 3 1]]


#========================
# Filtering Arrays (Boolean Masks)

# A boolean list/array picks the elements where the mask is True
arr = np.array([41, 42, 43, 44])
mask = arr > 42
print(mask)       # --> [False False  True  True]
print(arr[mask])  # --> [43 44]
