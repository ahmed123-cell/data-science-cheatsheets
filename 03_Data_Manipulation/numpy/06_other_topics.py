"""
NumPy Study Reference
=====================

A runnable, section-by-section walkthrough of NumPy fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Also            : statistics, linear algebra, NaN handling, broadcasting,
                    correlation and covariance
"""

import numpy as np


#========================
# Statistics

arr = np.array([48, 38, 23, 12, 39, 39, 23, 90, 2])

print(np.min(arr))     # --> 2
print(np.max(arr))     # --> 90

print(np.mean(arr))    # --> 34.888888888888886
print(np.median(arr))  # --> 38.0

# std / var use ddof=0 (population) by default; pass ddof=1 for a sample
print(np.std(arr))     # --> 23.899997417221822  (standard deviation)
print(np.var(arr))     # --> 571.2098765432098   (variance)


#========================
# Linear Algebra

# Dot product of two vectors: sum of element-wise products
vector1 = np.array([5, 3, 9, 1, 8, 3])
vector2 = np.array([3, 1, 8, 9, 3, 1])
print(np.dot(vector1, vector2))  # --> 126

# Matrix multiplication: (3x2) @ (2x3) gives a (3x3) matrix
matrix1 = np.array([[6, 4], [2, 1], [5, 5]])
matrix2 = np.array([[5, 7, 8], [9, 9, 0]])
print(np.matmul(matrix1, matrix2))
print(matrix1 @ matrix2)  # the @ operator does the same
# --> [[66 78 48]
#      [19 23 16]
#      [70 80 40]]

matrix = np.array([[4, 5], [9, 3]])
print(np.linalg.inv(matrix))   # --> inverse matrix
# --> [[-0.09090909  0.15151515]
#      [ 0.27272727 -0.12121212]]
print(np.linalg.eig(matrix))   # --> eigenvalues [10.22681202, -3.22681202] and the eigenvectors
print(np.linalg.norm(matrix))  # --> 11.445523142259598  (matrix length / Frobenius norm)
print(np.linalg.det(matrix))   # --> -33.000000000000014 (determinant, ~ -33 after rounding error)

print(np.eye(4))               # --> 4x4 identity matrix
print(np.diag([1, 2, 3, 4]))   # --> 4x4 matrix with these values on the diagonal

# solve(A, B) finds x in A @ x = B   ->   2x + 3y = 7 and x + 4y = 8
A = np.array([[2, 3], [1, 4]])
B = np.array([7, 8])
print(np.linalg.solve(A, B))  # --> [0.8 1.8]


#========================
# Handling NaN Values

arr = np.array([2, np.nan, 8, np.nan, 9])
print(np.isnan(arr))     # --> [False  True False  True False]
print(np.nanmean(arr))   # --> 6.333333333333333  (mean that ignores NaN)


#========================
# Broadcasting

# Broadcasting lets arrays of different shapes work together: the smaller
# array is "stretched" to match the larger one.

# A (3, 2) array plus a (2,) vector: the vector is added to every row
arr = np.array([[1, 2], [3, 4], [5, 6]])
vec = np.array([10, 20])
print(arr + vec)
# --> [[11 22]
#      [13 24]
#      [15 26]]

# A scalar is broadcast to every element
arr = np.array([1, 2, 3, 4])
print(arr * 2)  # --> [2 4 6 8]

# Boolean-mask assignment: update only the elements that match a condition
arr = np.array([1, 2, 3, 4, 5])
mask = arr % 2 == 0
arr[mask] = arr[mask] * 10
print(arr)  # --> [ 1 20  3 40  5]


#========================
# Correlation and Covariance

x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])  # y = 2x, a perfect positive linear relationship

# corrcoef: correlation matrix (1 = perfect positive, -1 = perfect negative)
print(np.corrcoef(x, y))
# --> [[1. 1.]
#      [1. 1.]]

# cov: covariance matrix. Diagonal = variances of x and y; the rest = their covariance.
# (rowvar=False has no effect here because x and y are 1D.)
print(np.cov(x, y, rowvar=False))
# --> [[1.66666667 3.33333333]
#      [3.33333333 6.66666667]]