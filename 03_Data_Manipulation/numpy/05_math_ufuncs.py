"""
NumPy Study Reference
=====================

A runnable, section-by-section walkthrough of NumPy fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Math (ufuncs)   : arithmetic, rounding, logs, sums, trigonometry, sets
"""

import numpy as np

#========================
# Custom ufuncs

# A ufunc ("universal function") applies an operation to every element of an
# array in a fast, vectorized way.

def square_plus_one(x):
    """Return x squared plus one."""
    return x**2 + 1

# frompyfunc(function, number_of_inputs, number_of_outputs)
square_plus_one_ufunc = np.frompyfunc(square_plus_one, 1, 1)
print(square_plus_one_ufunc(np.array([1, 2, 3, 4])))  # --> [2 5 10 17]

# Check whether a function is a real ufunc
print(type(np.add))          # --> <class 'numpy.ufunc'>
print(type(np.concatenate))  # --> <class 'numpy._ArrayFunctionDispatcher'> (not a ufunc)


#========================
# Arithmetic ufuncs

# add
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
print(np.add(arr1, arr2))  # --> [30 32 34 36 38 40]

# subtract and multiply (element by element)
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
print(np.subtract(arr1, arr2))  # --> [-10  -1   8  17  26  35]
print(np.multiply(arr1, arr2))  # --> [ 200  420  660  920 1200 1500]

# divide: always returns floats
arr2 = np.array([3, 5, 10, 8, 2, 33])
print(np.divide(arr1, arr2))
# --> [ 3.33333333  4.          3.          5.         25.          1.81818182]

# power: arr1[i] ** arr2[i]
arr1 = np.array([2, 4, 6, 7, 10])
arr2 = np.array([1, 2, 3, 4, 5])
print(np.power(arr1, arr2))  # --> [     2     16    216   2401 100000]

# remainder: mod and remainder do the same thing
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
print(np.mod(arr1, arr2))        # --> [ 1  6  3  0  0 27]
print(np.remainder(arr1, arr2))  # --> [ 1  6  3  0  0 27]

# divmod: returns two arrays, the quotients and the remainders
print(np.divmod(arr1, arr2))
# --> (array([ 3,  2,  3,  5, 25,  1]), array([ 1,  6,  3,  0,  0, 27]))

# absolute value
arr = np.array([-1, -2, 1, 2, 3, -4])
print(np.absolute(arr))  # --> [1 2 1 2 3 4]


#========================
# Rounding

# trunc: drops the decimal part (rounds toward zero)
print(np.trunc([-3.1666, 3.6667]))  # --> [-3.  3.]

# around: rounds to the given number of decimals (np.round is the same)
print(np.around(3.166666, 2))  # --> 3.17

# floor: rounds down to the nearest integer
print(np.floor([-3.1666, 3.6667]))  # --> [-4.  3.]

# ceil: rounds up to the nearest integer
print(np.ceil([-3.1666, 3.6667]))  # --> [-3.  4.]


#========================
# Logarithms and Exponents

print(np.log2([2, 4, 8, 16, 32]))   # --> [1. 2. 3. 4. 5.]     (base 2)
print(np.log10([1, 10, 100, 1000])) # --> [0. 1. 2. 3.]        (base 10)
print(np.log([4, 8, 12]))           # --> [1.38629436 2.07944154 2.48490665]  (base e)

print(np.exp(5))   # --> 148.4131591025766   (e ** 5)
print(np.exp2(5))  # --> 32.0                (2 ** 5)


#========================
# Sums, Products, and Differences

# sum: no axis = everything, axis=0 = down the columns, axis=1 = across the rows
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
print(np.sum([arr1, arr2]))          # --> 12
print(np.sum([arr1, arr2], axis=1))  # --> [6 6]     (sum of each row)
print(np.sum([arr1, arr2], axis=0))  # --> [2 4 6]   (sum of each column)

# cumsum: running total
arr = np.array([1, 2, 3, 4])
print(np.cumsum(arr))  # --> [ 1  3  6 10]

# prod: product of all elements (optionally along an axis)
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
print(np.prod([arr1, arr2]))          # --> 40320
print(np.prod([arr1, arr2], axis=1))  # --> [  24 1680]

# cumprod: running product
arr = np.array([5, 6, 7, 8])
print(np.cumprod(arr))  # --> [   5   30  210 1680]

# diff: difference between neighbouring elements; n = how many times to repeat
arr = np.array([10, 15, 25, 5])
print(np.diff(arr))       # --> [  5  10 -20]
print(np.diff(arr, n=2))  # --> [  5 -30]


#========================
# LCM and GCD

# lcm: lowest common multiple
print(np.lcm(4, 6))                         # --> 12
print(np.lcm.reduce(np.array([3, 6, 9])))   # --> 18  (across a whole array)

# gcd: greatest common divisor
print(np.gcd(9, 6))                          # --> 3
print(np.gcd.reduce([20, 8, 32, 36, 16]))    # --> 4   (across a whole array)


#========================
# Logical Reductions

# all: True only if EVERY element is True. any: True if AT LEAST ONE is True
arr = np.array([[True, False, False], [True, False, True]])
print(np.all(arr))  # --> False
print(np.any(arr))  # --> True


#========================
# Trigonometry

angles = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])  # in radians

print(np.sin(angles))  # --> [1.         0.8660254  0.70710678 0.58778525]
print(np.cos(angles))  # --> [6.12323400e-17 5.00000000e-01 7.07106781e-01 8.09016994e-01]
print(np.tan(angles))  # --> [1.63312394e+16 1.73205081e+00 1.00000000e+00 7.26542528e-01]
# Floating-point note: cos(pi/2) is exactly 0 and tan(pi/2) is undefined in
# maths, but pi cannot be stored exactly, so tiny/huge values appear instead.

# Convert between degrees and radians
print(np.deg2rad(np.array([90, 180, 270, 360])))
# --> [1.57079633 3.14159265 4.71238898 6.28318531]
print(np.rad2deg(np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])))
# --> [ 90. 180. 270. 360.]

# Inverse functions find the angle (in radians): arcsin, arccos, arctan
print(np.arcsin(1.0))  # --> 1.5707963267948966  (pi / 2)

# hypot: hypotenuse of a right triangle (Pythagorean theorem)
base, perp = 4, 3
print(np.hypot(base, perp))  # --> 5.0


#========================
# Set Operations

# unique: sorted values with duplicates removed
print(np.unique([1, 1, 1, 2, 3, 4, 5, 5, 6, 7]))  # --> [1 2 3 4 5 6 7]

# assume_unique=True speeds things up when the inputs have no duplicates
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

print(np.union1d(arr1, arr2))                          # --> [1 2 3 4 5 6]  union
print(np.intersect1d(arr1, arr2, assume_unique=True))  # --> [3 4]          intersection
print(np.setdiff1d(arr1, arr2, assume_unique=True))    # --> [1 2]          in arr1 only
print(np.setxor1d(arr1, arr2, assume_unique=True))     # --> [1 2 5 6]      symmetric difference