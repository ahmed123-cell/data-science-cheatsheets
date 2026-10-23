"""
NumPy Study Reference
=====================

A runnable, section-by-section walkthrough of NumPy fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Array basics    : creation, dimensions, indexing, data types, copy vs view
"""

import numpy as np

#========================
# Creating Arrays

arr = np.array([1, 2, 3])
print(arr)        # --> [1 2 3]
print(type(arr))  # --> <class 'numpy.ndarray'>


#========================
# Array Dimensions

# ndim is the number of dimensions (axes): scalar = 0, vector = 1, matrix = 2, ...
print(np.array(42).ndim)                                      # --> 0
print(np.array([21, 89, 37, 29]).ndim)                        # --> 1
print(np.array([[1, 2, 3], [1, 2, 3]]).ndim)                  # --> 2
print(np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]).ndim)    # --> 3

# ndmin forces a minimum number of dimensions by adding leading axes
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)       # --> [[[[[1 2 3 4]]]]]
print(arr.ndim)  # --> 5


#========================
# Array Creation Functions

print(np.zeros((2, 3)))
# --> [[0. 0. 0.]
#      [0. 0. 0.]]

print(np.ones((2, 3)))
# --> [[1. 1. 1.]
#      [1. 1. 1.]]

# fill_value=None creates an object array whose cells all hold None
print(np.full((2, 3), fill_value=None))
# --> [[None None None]
#      [None None None]]

# arange(start, stop): the stop value is excluded
print(np.arange(1, 20))  # --> [ 1  2  3 ... 18 19]

# linspace(start, stop, count): `count` evenly spaced values, stop included
print(np.linspace(1, 10, 5))  # --> [ 1.    3.25  5.5   7.75 10.  ]


#========================
# Indexing and Slicing

# 1D: indexes start at 0. Slices use start:stop:step (stop excluded)
arr = np.array([1, 2, 3, 4])
print(arr[0])        # --> 1
print(arr[1])        # --> 2
print(arr[2] + arr[3])  # --> 7
print(arr[1:4:2])    # --> [2 4]

# 2D: arr[row, column]
arr_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr_2d[0, 1])      # --> 2
print(arr_2d[1, 1:4])    # --> [7 8 9]
print(arr_2d[0:2, 2])    # --> [3 8]    (column 2 from both rows)
print(arr_2d[0:2, 1:4])
# --> [[2 3 4]
#      [7 8 9]]

# 3D: arr[block, row, column]
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr_3d[0, 1, 2])    # --> 6
print(arr_3d[0, 1, 0:2])  # --> [4 5]


#========================
# Data Types

# Every array holds a single dtype. The default integer type is platform dependent
print(np.array([1, 2, 3]).dtype)                      # --> int64
print(np.array(['orange', 'banana', 'apple']).dtype)  # --> <U6  (unicode, up to 6 chars)

# Set the dtype explicitly with a type code: 'S' = bytes string, 'i4' = 4-byte int
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)        # --> [b'1' b'2' b'3' b'4']
print(arr.dtype)  # --> |S1

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)        # --> [1 2 3 4]
print(arr.dtype)  # --> int32

# nbytes: memory used by the data (5 elements x 8 bytes for int64)
arr = np.array([1, 2, 3, 4, 5])
print(arr.nbytes)  # --> 40


#========================
# Converting Data Types

# astype() returns a new array with the requested dtype
arr = np.array([2.1, 4.7, 1.9])
new_arr = arr.astype(int)  # floats are truncated, not rounded
print(new_arr)        # --> [2 4 1]
print(new_arr.dtype)  # --> int64

arr = np.array([1, 0, 3])
new_arr = arr.astype(bool)  # 0 becomes False, any other number becomes True
print(new_arr)        # --> [ True False  True]
print(new_arr.dtype)  # --> bool


#========================
# Copy vs View

# Copy: a new array with its own data. Changes do NOT affect the original.
arr = np.array([1, 2, 3, 4])
arr_copy = arr.copy()
arr_copy[0] = 42
print(arr)       # --> [1 2 3 4]
print(arr_copy)  # --> [42  2  3  4]

# View: a new array object that shares the original's data (no copy is made).
# Changes made through the view DO affect the original, and vice versa.
arr = np.array([1, 2, 3, 4])
arr_view = arr.view()
arr_view[1] = 38
print(arr)       # --> [ 1 38  3  4]
print(arr_view)  # --> [ 1 38  3  4]

# .base tells whether an array owns its data
print(arr_copy.base)  # --> None  (the copy owns its data)
print(arr_view.base)  # --> [ 1 38  3  4]  (the view points to the original array)