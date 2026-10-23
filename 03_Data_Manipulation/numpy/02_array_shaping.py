"""
NumPy Study Reference
=====================

A runnable, section-by-section walkthrough of NumPy fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Array shaping   : reshape, flatten, transpose, iterate, join, split
"""

import numpy as np

#========================
# Array Shape and Reshaping

# shape: the number of elements in each dimension
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)  # --> (2, 4)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr.shape)  # --> (1, 1, 1, 1, 4)

# reshape: change dimensions as long as the element count stays the same
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(arr.reshape(4, 3))
# --> [[ 1  2  3]
#      [ 4  5  6]
#      [ 7  8  9]
#      [10 11 12]]

print(arr.reshape(2, 3, 2))
# --> [[[ 1  2]
#       [ 3  4]
#       [ 5  6]]
#
#      [[ 7  8]
#       [ 9 10]
#       [11 12]]]

# reshape returns a view when possible, so .base is the original array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)  # --> [1 2 3 4 5 6 7 8]

# One dimension may be -1 ("unknown"): NumPy calculates it for you
print(arr.reshape(2, 2, -1))   # --> shape (2, 2, 2)
# --> [[[1 2]
#       [3 4]]
#
#      [[5 6]
#       [7 8]]]

# reshape(-1) flattens any array into 1D
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.reshape(-1))  # --> [1 2 3 4 5 6]


#========================
# Flatten, Transpose, and Reorder

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr.flatten())  # --> [1 2 3 4 5 6 7 8 9]   (always returns a copy)
print(arr.ravel())    # --> [1 2 3 4 5 6 7 8 9]   (returns a view when possible)

# transpose swaps rows and columns; .T is the shorthand
print(arr.transpose())
print(arr.T)
# --> [[1 4 7]
#      [2 5 8]
#      [3 6 9]]

# expand_dims adds a new axis; squeeze removes axes of length 1
print(np.expand_dims([1, 2, 3, 4, 5], axis=0).shape)  # --> (1, 5)
print(np.expand_dims([1, 2, 3, 4, 5], axis=1).shape)  # --> (5, 1)
print(np.array([[[1], [2]], [[3], [4]]]).shape)       # --> (2, 2, 1)
print(np.squeeze([[[1], [2]], [[3], [4]]]).shape)     # --> (2, 2)

# flip reverses the order of elements along an axis (all axes if none is given)
arr = np.array([1, 2, 3, 4])
print(np.flip(arr))  # --> [4 3 2 1]

arr_2d = np.array([[1, 2], [3, 4]])
print(np.flip(arr_2d, axis=0))  # --> [[3 4] [1 2]]   (reverse the rows)
print(np.flip(arr_2d, axis=1))  # --> [[2 1] [4 3]]   (reverse the columns)

# NOTE: NumPy has many more shape/reordering tools (rot90, fliplr, flipud, ...).
# They belong to the intermediate-to-advanced level.


#========================
# Iterating Over Arrays

# A plain for-loop needs one loop per dimension. nditer visits every scalar
# of an n-dimensional array with a single loop.
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for value in np.nditer(arr):
    print(value)  # --> 1 2 3 4 5 6 7 8 (one per line)

# Iterate while converting the dtype on the fly (requires the 'buffered' flag)
arr = np.array([1, 2, 3])
for value in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(value)  # --> b'1', b'2', b'3'  (NumPy 2.x shows np.bytes_(b'1'), ...)

# Iterate over a slice: every second column
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for value in np.nditer(arr[:, ::2]):
    print(value)  # --> 1 3 5 7 (one per line)

# ndenumerate yields (index, value) pairs
arr = np.array([1, 2, 3])
for index, value in np.ndenumerate(arr):
    print(index, value)  # --> (0,) 1 / (1,) 2 / (2,) 3

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for index, value in np.ndenumerate(arr):
    print(index, value)  # --> (0, 0) 1 / (0, 1) 2 / ... / (1, 3) 8


#========================
# Joining Arrays

# concatenate joins along an existing axis (axis=0 by default)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.concatenate((arr1, arr2)))  # --> [1 2 3 4 5 6]

arr1 = np.array([[1, 2], [4, 5]])
arr2 = np.array([[7, 8], [9, 10]])
print(np.concatenate((arr1, arr2), axis=1))
# --> [[ 1  2  7  8]
#      [ 4  5  9 10]]

# stack is like concatenate, but joins along a NEW axis (default axis=0).
# Stacking two 1D arrays on axis=1 pairs up their elements.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(np.stack((arr1, arr2), axis=1))
# --> [[1 4]
#      [2 5]
#      [3 6]]

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# hstack: join horizontally (end to end)
print(np.hstack((arr1, arr2)))  # --> [1 2 3 4 5 6 7 8]

# vstack: join vertically (each array becomes a row)
print(np.vstack((arr1, arr2)))
# --> [[1 2 3 4]
#      [5 6 7 8]]

# dstack: join along depth (the 3rd axis), result shape is (1, 4, 2)
print(np.dstack((arr1, arr2)))
# --> [[[1 5]
#       [2 6]
#       [3 7]
#       [4 8]]]

# column_stack (or np.c_) turns 1D arrays into the columns of a 2D array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.c_[a, b])
print(np.column_stack((a, b)))
# --> [[1 4]
#      [2 5]
#      [3 6]]


#========================
# Splitting Arrays

# array_split(array, parts) returns a list of sub-arrays
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.array_split(arr, 3))  # --> [array([1, 2]), array([3, 4]), array([5, 6])]

# If the array does not divide evenly, the first parts get the extra elements
print(np.array_split(arr, 4))  # --> [array([1, 2]), array([3, 4]), array([5]), array([6])]

# Split at given indexes: here at 12 and 16 -> arr[:12], arr[12:16], arr[16:]
arr = np.arange(1, 21)  # 1..20
print(np.array_split(arr, [12, 16]))
# --> [array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]),
#      array([13, 14, 15, 16]),
#      array([17, 18, 19, 20])]

# Split a 2D array by columns (axis=1): three arrays, each of shape (6, 1)
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12],
                [13, 14, 15],
                [16, 17, 18]])
print(np.array_split(arr, 3, axis=1))
# --> [array([[ 1], [ 4], [ 7], [10], [13], [16]]),   (column 0)
#      array([[ 2], [ 5], [ 8], [11], [14], [17]]),   (column 1)
#      array([[ 3], [ 6], [ 9], [12], [15], [18]])]   (column 2)

# hsplit splits by columns too (the parts must divide evenly). Same result as above
print(np.hsplit(arr, 3))