import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create an array
arr = np.array([1, 2, 3])
print(arr) # --> [1 2 3]
print(type(arr)) # --> <class 'numpy.ndarray'>
#------------------------------------------------
# Dimension of the array
print(np.array(42).ndim) # --> 0
print(np.array([21, 89, 37, 29]).ndim) # --> 1
print(np.array([[1, 2, 3], [1, 2, 3]]).ndim) # --> 2
print(np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]).ndim) # --> 3

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr) # --> [[[[[1 2 3 4]]]]]
print(arr.ndim) # --> 5
#-------------------------------------------------------------------
# Access Array elements
arr = np.array([1, 2, 3, 4])
print(arr[0]), print(arr[1]) # --> 1, 2
print(arr[2] + arr[3]) # --> 7
print(arr[1:4:2]) # --> [2, 4]

# access 2D array
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0, 1])# --> 2 
print(arr[1, 1:4]) # --> [7, 8, 9]

# access 3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) # --> 6
print(arr[0, 1, 0:2]) # --> [4, 5]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2]) # --> [3, 8]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4]) # --> [[2, 3, 4], [7, 8, 9]]
#=-----------------------------------------------------------------------------------
# Numpy Data types
print(np.array([1, 2, 3]).dtype) # --> int64
print(np.array(['orange', 'banana', 'apple']).dtype) # --> <U6

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr) # --> [b'1' b'2' b'3' b'4']
print(arr.dtype) # --> |S1

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr) # --> [1 2 3 4]
print(arr.dtype) # --> int32

# return memory bytes
a = np.array([1, 2, 3, 4, 5])
print(a.nbytes) # --> 40
#--------------------------------------------
# Convert data type on exist array
arr = np.array([2.1, 4.7, 1.9])
new_arr = arr.astype(int)
print(new_arr) # --> [2 4 1]
print(new_arr.dtype) # --> int64

arr = np.array([1, 0, 3])
new_arr = arr.astype(bool)
print(new_arr)  # --> [ True False  True]
print(new_arr.dtype) # --> bool
#---------------------------------------------
# Numpy array Copy & view

# Copy: A copy is a new array with its own independent data. It does not share memory with the original array. It does not affect on orignal array
arr = np.array([1, 2, 3, 4])
x = arr.copy()
x[0] = 42
print(arr), print(x) # --> [1 2 3 4], [42  2  3  4]

# View: A view is a new array object that refers to the same data as the original array (shallow copy)
# It does not own the data but shares with the original data. And it affects on original array and has the same memory location
arr = np.array([1, 2, 3, 4])
y = arr.view()
y[1] = 38
print(arr), print(y) # --> [ 1 38  3  4], [ 1 38  3  4]

# check if the array owns its data
print(x.base) # --> None (array x owns its data)
print(y.base) # --> Original Data (array y does not own its data)
#-------------------------------------------------------------------------
# Shape of the array
# shape : The shape of an array is the number of elements in each dimension.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) # --> (2, 4)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr.shape) # --> ((1, 1, 1, 1, 4))

# Reshape the arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr.reshape(4, 3)
print(new_arr) # --> [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

new_arr2 = arr.reshape(2, 3, 2)
print(new_arr2) # --> [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]]

# Copy or View
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base) # --> orignal array (View)

# Unknown Dimension: You are allowed to have one "unknown" dimension.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr = arr.reshape(2, 2, -1)
print(new_arr) # --> [[[1, 2], [3, 4]], [5, 6], [7, 8]]

# Flatten the array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
new_arr = arr.reshape(-1)
print(new_arr) # --> [1, 2, 3, 4, 5, 6]

# NOTE: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel
# and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.
#------------------------------------------------------------------------------
# iterate arrays
# Iterating through each scaler needs n of for loops which can be difficult to write for arrays with very high dimensionality.
# we use nditer to solve the problem
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

# Iterating Array With Different Data Types
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# Iterating With Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for num in np.nditer(arr[:, ::2]):
    print(num)

# Enumerated Iteration Using ndenumerate()
arr = np.array([1, 2, 3])
for index, x in np.ndenumerate(arr):
    print(index, x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
#--------------------------------------------------------------------------------
# Joining NumPy Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2)) # axis automacilly zero
print(arr) # --> [1, 2, 3, 4, 6]

arr1 = np.array([[1, 2], [4, 5]])
arr2 = np.array([[7, 8], [9, 10]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr) # --> [[1, 2, 7, 8], [4, 5, 9, 10]]

"""
Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr) # --> [[1, 4], [2, 5], [3, 6]]

# stacking along rows
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr = np.hstack((arr1, arr2))
print(arr) # --> [1 2 3 4 5 6 7 8]

# stacking along columns
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr = np.vstack((arr1, arr2))
print(arr) # --> [[1, 2, 3, 4], [5, 6, 7, 8]]

# Stacking Along Height (depth)
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr = np.dstack((arr1, arr2))
print(arr) # --> [[1, 5], [2, 6], [3, 7], [4, 8]]
#-----------------------------------------------------------
# Split the array
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 3)
print(new_arr) # --> [array([1, 2]), array([3, 4]), array([5, 6])]

# If the array has less elements than required, it will adjust from the end accordingly.
arr = np.array([1, 2, 3, 4, 5, 6])
new_arr = np.array_split(arr, 4)
print(new_arr) # --> [array([1, 2]), array([3, 4]), array([5]), array([6])]

# split array by sections
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(np.array_split(arr, [12, 16])) # --> [array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]), array([13, 14, 15, 16]), array([17, 18, 19, 20])]

# Split arrays by columns
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr) # --> [array([1], [4], [7], [10], [13], [16]), array([2], [5], [8], [11], [14], [17]),array([3], [6], [9], [12], [15], [18])]

# Split arrays by columns using hsplit
newarr = np.hsplit(arr, 3)
print(newarr)
#--------------------------------------------------------------------------
# Numpy Searching arrays

arr = np.array([1, 2, 3, 4, 5, 4, 4])
print(np.where(arr == 4)) # --> (array[3, 5, 6])
print(np.where(arr % 2 == 0)) # --> (array[1, 3, 5, 6])

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.where(arr == 4)) # --> (array([0]), array([3]))
print(np.where(arr % 2 == 0)) # --> (array([0, 0, 1, 1]), array([1, 3, 1, 3]))

# replace the element using where
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr = np.where(arr < 4, 0, arr)
print(arr)

# Searchsorted: performs a binary search in the array, and returns the index where the value would be inserted to maintain the search order.
arr = np.array([6, 7, 8, 9])
print(np.searchsorted(arr, 7)) # --> 1 (begin search from the left)
print(np.searchsorted(arr, 7, side='right')) # --> 2 (begin search from the right)

# Multiple values
arr = np.array([1, 3, 5, 7, 9])
print(np.searchsorted(arr, [2, 4, 6])) # --> [1 2 3]

# argsort: returns the indices that arrange the array
arr = np.array([3, 1, 4, 2])
print(np.argsort(arr)) # --> [1, 3, 0, 2]

# arrange the array in terms of first first column
arr2 = np.array([[9, 3, 1], [7, 4, 2], [0, 5, 3]])
print(arr2[arr2[:, 0].argsort()])
#--------------------------------------------------------------------------
# Sorting Arrays
print(np.sort(np.array([3, 2, 0, 1]))) # --> [0 1 2 3]
print(np.sort(np.array(['banana', 'apple', 'orange']))) #--> ['apple' 'banana' 'orange']
print(np.sort(np.array([True, False, True]))) # --> [False  True  True]

print(np.sort(np.array([[3, 2, 4], [5, 0, 1]]))) # --> [[2, 3, 4], [0, 1, 5]]

# sort by columns
print(np.sort(np.array([[3, 2, 4],
                        [5, 0, 1]]), axis=0)) # --> [[3, 0, 1], [5, 2, 4]]
#--------------------------------------------------------------------------
# Filtering arrays
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]

print(filter_arr) # --> [False False  True  True]
print(newarr) # --> [43 44]
#------------------------------------------------------------------------------------------------------------------
# Random numbers in Numpy
print(np.random.randint(100)) # random number from zero to 100
print(np.random.randint(100, size=(5))) # --> 1D array has 5 elements random numbers
print(np.random.randint(100, size=(3, 5))) # --> 2D array has 3 rows and 5 columns

print(np.random.rand()) # random float number from zero to one
print(np.random.rand(5)) # --> 1D array has 5 random float numbers
print(np.random.rand(3, 5)) # --> 2D array has 3 rows and 5 columns

print(np.random.randn(5)) # --> random normal distribution with five elemnets
print(np.random.randn(2, 3)) # --> 2D array has 3 rows and 5 columns

print(np.random.choice([2, 4, 6, 7])) # --> random value based on the array
print(np.random.choice([1, 2, 3, 8], size=(3, 3))) # --> 2D array has 3 rows and 3 columns

np.random.seed(42) # the origin to begin random values (psuedo random algorithm)
print(np.random.randint(1, 10, size=5)) # --> [7 4 8 5 7]
print(np.random.randint(1, 10, size=5)) # --> [7 4 8 5 7]
#------------------------------------------------------------------------------------------------------------------
# Random Data Distribution
data = np.random.choice([1, 2, 3, 4], p=[0.3, 0.2, 0.4, 0.1], size=(50))
data = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(6, 6))
#------------------------------------------------------------------------------------------------------------------
# Random Permutations
# shuffle: changes the arrangement of the original array
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)

# Permutation: re_arranged the array but it does not affect on original array
arr = np.array([1, 2, 3, 4, 5])
print(np.random.permutation(arr))
#------------------------------------------------------------------------------------------------------------------
# Visualize Distributions
sns.displot([0, 1, 2, 3, 4, 5])
plt.show() # --> histogram

sns.displot([0, 1, 2, 3, 4, 5], kind='kde')
plt.show() # --> curve
#------------------------------------------------------------------------------------------------------------------
# Normal Distribution
x = np.random.normal(loc= 1, scale= 2, size=(2, 3))
print(x) # --> normal disribution with size (2, 3) with mean: 1 and std: 2

# Visulize normal distribution
x = np.random.normal(size=(100))
sns.displot(x, kind='kde')
plt.show()
#------------------------------------------------------------------------------------------------------------------
# Binomial Distribution
x = np.random.binomial(n=10, p=0.5, size=(10))
print(x)

# Visulize Binomial Distribution
sns.displot(np.random.binomial(n=10, p=0.5, size=1000))
plt.show()

# Difference Between Normal and Binomial Distribution
data = {
  "normal": np.random.normal(loc=50, scale=5, size=1000),
  "binomial": np.random.binomial(n=100, p=0.5, size=1000)
}
sns.displot(data, kind="kde")
plt.show()
#------------------------------------------------------------------------------------------------------------------
# Poisson Distribution
x = np.random.poisson(lam=2, size=10)
print(x)

# Visulize poisson Distribution
sns.displot(np.random.poisson(lam=2, size=1000))
plt.show()

# Difference Between Normal and Poisson Distribution
data = {
  "normal": np.random.normal(loc=50, scale=7, size=1000),
  "poisson": np.random.poisson(lam=50, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

# Difference Between Binomial and Poisson Distribution
data = {
  "binomial": np.random.binomial(n=1000, p=0.01, size=1000),
  "poisson": np.random.poisson(lam=10, size=1000)
}
sns.displot(data, kind="kde")
plt.show()
#------------------------------------------------------------------------------------------------------------------
# Uniform Distribution
x = np.random.uniform(low= 0.0, high=1.0, size=(2, 3))

# Visulize Uniform Distribution
sns.displot(np.random.uniform(size=1000), kind="kde")
plt.show()
#------------------------------------------------------------------------------------------------------------------
# Logistic Distribution: used in machine learning and neural networks
x = np.random.logistic(loc=1, scale=2, size=(2, 3))

# Visulize Logistic Distribution
sns.displot(np.random.logistic(size=1000), kind="kde")
plt.show()
#------------------------------------------------------------------------------------------------------------------
# Multinomial Distribution: generalization of binomial distribution
x = np.random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(2, 3))
print(x) # --> Multinomial samples will NOT produce a single value! They will produce one value for each pval
#------------------------------------------------------------------------------------------------------------------
# Exponential Distribution
x = np.random.exponential(scale=2, size=(2, 3))
print(x)

# Visulize exponential distribution
sns.displot(np.random.exponential(size=1000), kind='kde')
plt.show()
#------------------------------------------------------------------------------------------------------------------
# Chi square Distribution
x = np.random.chisquare(df=2, size=(2, 3))
print(x)

# Visulize chi square distribution
sns.displot(np.random.chisquare(df=1, size=1000), kind='kde')
plt.show()
#------------------------------------------------------------------------------------------------------------------
# Numpy ufuncs

# Create a numpy function: frompyfunc(func, num_input, num_output)
arr = np.array([1, 2, 3, 4])
def operation(x):
    return x**2 + 1
my_opeartion = np.frompyfunc(operation, 1, 1)
print(my_opeartion(arr)) # --> [2 5 10 17]

print(type(np.add)) # --> <class 'numpy.ufunc'>
print(type(np.concatenate)) # --> <class 'numpy._ArrayFunctionDispatcher'>

""" Famous Numpy ufuncs """
# add
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
print(np.add(arr1, arr2)) # --> [30 32 34 36 38 40]

# substract
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
print(np.subtract(arr1, arr2)) # --> [-10  -1   8  17  26  35]

# multiply
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])
print(np.multiply(arr1, arr2)) # --> [ 200  420  660  920 1200 1500]

# divide
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])
print(np.divide(arr1, arr2)) # --> [ 3.33333333  4.          3.          5.         25.          1.81818182]

# power
arr1 = np.array([2, 4, 6, 7, 10])
arr2 = np.array([1, 2, 3, 4, 5])
print(np.power(arr1, arr2)) # --> [     2     16    216   2401 100000]

# remainder
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
print(np.mod(arr1, arr2)) # --> [ 1  6  3  0  0 27]
print(np.remainder(arr1, arr2)) # --> [ 1  6  3  0  0 27]

# divmod : returns an array one with quotient and another array with mod
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])
print(np.divmod(arr1, arr2)) # --> (array([ 3,  2,  3,  5, 25,  1]), array([ 1,  6,  3,  0,  0, 27]))

# absulote value
arr = np.array([-1, -2, 1, 2, 3, -4])
print(np.absolute(arr)) # --> [1, 2, 1, 2, 3, 4]

# truncate: remove float part of the number and return intergers
print(np.trunc([-3.1666, 3.6667])) # --> [-3. 3.]

# round
print(np.around(3.166666, 2)) # --> 3.17

# floor
print(np.floor([-3.1666, 3.6667])) # --> [-4.  3.]

# ceil
print(np.ceil([-3.1666, 3.6667])) # --> [-3.  4.]

# log2
print(np.log2([2 , 4, 8, 16, 32])) # --> [1. 2. 3. 4. 5.]

# log10
print(np.log10([1, 10, 100, 1000])) # --> [0. 1. 2. 3. 4.]

# log at base e
print(np.log([4, 8, 12])) # --> [1.38629436 2.07944154 2.48490665]

# exp
print(np.exp(5)) # --> 148.4131591025766

# exp2
print(np.exp2(5)) # --> 32.0

# sum
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
print(np.sum([arr1, arr2])) # --> 12
print(np.sum([arr1, arr2], axis= 1)) # --> [6, 6] --> sum by rows
print(np.sum([arr1, arr2], axis= 0)) # --> [2, 4, 6] --> sum by columns

# cumumlative sum
arr = np.array([1, 2, 3, 4])
print(np.cumsum(arr)) # --> [1 3 6 10]

# prod
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
print(np.prod([arr1, arr2])) # --> 40320
print(np.prod([arr1, arr2], axis=1)) # --> [24 1680]

# cummulative prod
arr = np.array([5, 6, 7, 8])
print(np.cumprod(arr)) # --> [5 30 210 1680]

# diff
arr = np.array([10, 15, 25, 5])
print(np.diff(arr)) # --> [5 10 -20]
print(np.diff(arr, n=2)) # --> [5 -30] --> n refers to repeat this operation number of times

# lcm
num1, num2 = 4, 6
print(np.lcm(num1, num2)) # --> 12
print(np.lcm.reduce(np.array([3, 6, 9]))) # --> 18

# gcd
num1, num2 = 9, 6
print(np.gcd(num1, num2)) # --> 3
print(np.gcd.reduce([20, 8, 32, 36, 16])) # --> 4

# all
arr = np.array([[True, False, False], [True, False, True]])
print(np.all(arr)) # --> False

# any
arr = np.array([[True, False, False], [True, False, True]])
print(np.any(arr)) # True

# Trigonometric Functions
print(np.sin(np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5]))) # --> [1.    0.8660254  0.70710678 0.58778525]
print(np.cos(np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5]))) # --> [6.12323400e-17 5.00000000e-01 7.07106781e-01 8.09016994e-01]
print(np.tan(np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5]))) # --> [1.63312394e+16 1.73205081e+00 1.00000000e+00 7.26542528e-01]

# Degrees to Radinas and vice versa
print(np.deg2rad(np.array([90, 180, 270, 360]))) # --> [1.57079633 3.14159265 4.71238898 6.28318531]
print(np.rad2deg(np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi]))) # --> [ 90. 180. 270. 360.]

# find angeles : (arcsin, arccos, arctan)
print(np.arcsin(1.0)) # --> 1.5707963267948966

# find Hypotenues: pythagoras theorem
base, perp = 4, 3
print(np.hypot(4, 3)) # --> 5

# Sets in numpy and its operations
x = np.unique([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
print(x) # --> [1 2 3 4 5 6 7]

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

print(np.union1d(arr1, arr2)) # --> [1, 2, 3, 4, 5, 6] --> union
print(np.intersect1d(arr1, arr2, assume_unique=True)) # --> [3, 4] --> intersection
print(np.setdiff1d(arr1, arr2, assume_unique=True)) # --> [1, 2] --> difference
print(np.setxor1d(arr1, arr2, assume_unique=True)) # --> [1, 2, 5, 6] --> symmetric difference
#--------------------------------------------------------------------------------------------------------------------------------
# some numpy built in functions
print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.full((2, 3), fill_value=None))
print(np.arange(1, 20))
print(np.linspace(1, 10, 5))

# reshape and reaarrange the array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr.flatten()) # --> converts a copy of flatten array
print(arr.ravel()) # --> converts a view of flatten array
print(arr.transpose()), print(arr.T) # --> transpose the array

# control in dimensions
print(np.expand_dims([1, 2, 3, 4, 5], axis=0).shape)
print(np.expand_dims([1, 2, 3, 4, 5], axis=1).shape)

print(np.array([[[1], [2]], [[3], [4]]]).shape)
print(np.squeeze([[[1], [2]], [[3], [4]]]).shape)
#---------------------------------------------------------------------------------
# Numpy with statistics
arr = np.array([48, 38, 23, 12, 39, 39, 23, 90, 2])
print(np.min(arr)), print(np.max(arr)) # --> min, max

print(np.mean(arr)), print(np.median(arr)) # --> mean, median

print(np.std(arr)), print(np.var(arr)) # --> standard deviation, variance
# ddof arg. : degrees of freedom
#---------------------------------------------------------------------------------
# flip: reverse the arrangnement of rows or columns or entire array
arr = np.array([1, 2, 3, 4])
print(np.flip(arr)) # --> [4, 3, 2, 1]

arr_2d = np.array([[1, 2], [3, 4]])
print(np.flip(arr_2d, axis=0)) # --> [[3, 4], [1, 2]]
print(np.flip(arr_2d, axis=1)) # --> [[2, 1], [4, 3]]
#---------------------------------------------------------------------------------
# Numpy with Linear Algebra
vector1 = np.array([5, 3, 9, 1, 8, 3])
vector2 = np.array([3, 1, 8, 9, 3, 1])
print(np.dot(vector1, vector2)) # --> dot product

matrix1 = np.array([[6, 4], [2, 1], [5, 5]])
matrix2 = np.array([[5, 7, 8], [9, 9, 0]])
print(np.matmul(matrix1, matrix2))
print(matrix1 @ matrix2) # matrix multiplication

matrix = np.array([[4, 5], [9, 3]])
print(np.linalg.inv(matrix)) # --> inverse of matrix
print(np.linalg.eig(matrix)) # --> eigen values and eigen vectors
print(np.linalg.norm(matrix)) # --> length (vector or matrix)
print(np.linalg.det(matrix)) # --> -33 (determent of matrix)

print(np.eye(4)) # --> create identity matrix
print(np.diag([1, 2, 3, 4])) # --> construct diagonal matrix

A = np.array([[2, 3], [1, 4]])
B = np.array([7, 8])
print(np.linalg.solve(A, B)) # --> [0.8, 1.8]: (Ax = B)
#---------------------------------------------------------------------
# Dealing with Nan values
arr = np.array([2, np.nan, 8, np.nan, 9])
print(np.isnan(arr))
print(np.nanmean(arr)) # --> 6.333333333333333
#---------------------------------------------------------------------
# Broadcasting:
arr = np.array([[1, 2], [3, 4], [5, 6]])
vec = np.array([10, 20])
print(arr + vec) # --> [[11, 22], [13, 24], [15, 26]]

arr = np.array([1, 2, 3, 4])
print(arr * 2) # --> [2, 4, 6, 8]

# broadcasting with filtered elements:
arr = np.array([1, 2, 3, 4, 5])
mask = (arr % 2 == 0)
arr[mask] = arr[mask] * 10
print(arr) # --> [1, 20, 3, 40, 5]
#-----------------------------------------------------------------------
# correlation and convariance between data:
x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])
print(np.corrcoef(x, y)) # --> positve correlation
print(np.cov(x, y, rowvar=False)) # --> covariance
#-----------------------------------------------------------------------
# column stack
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.c_[a, b])
print(np.column_stack((a, b)))