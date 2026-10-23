"""
NumPy Study Reference
=====================

A runnable, section-by-section walkthrough of NumPy fundamentals. For each
example: read the comment, run the code, then compare with the ``# -->`` note
that shows the expected output.

Topics covered
--------------
* Random numbers  : basics, seeding, permutations, common distributions

Notes
-----
* Sample outputs were produced with NumPy 2.x on 64-bit Linux. A few details
  vary by version or platform (e.g. NumPy 1.x on Windows defaults to int32).
* Unseeded random examples differ on every run, so their comments describe
  the shape and range of the result instead of exact numbers.
* The plotting sections call ``plt.show()``; close each plot window to continue.
* This file uses the legacy ``np.random`` functions, as the original tutorial
  did. Newer code usually prefers ``np.random.default_rng()``.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#========================
# Random Numbers

# randint(high): integer from 0 up to high - 1
print(np.random.randint(100))                # --> a single int in 0..99
print(np.random.randint(100, size=5))        # --> 1D array of 5 ints
print(np.random.randint(100, size=(3, 5)))   # --> 2D array: 3 rows x 5 columns

# rand: floats from 0 (inclusive) to 1 (exclusive)
print(np.random.rand())         # --> a single float
print(np.random.rand(5))        # --> 1D array of 5 floats
print(np.random.rand(3, 5))     # --> 2D array: 3 rows x 5 columns

# randn: samples from the standard normal distribution (mean 0, std 1)
print(np.random.randn(5))       # --> 1D array of 5 values
print(np.random.randn(2, 3))    # --> 2D array: 2 rows x 3 columns

# choice: picks values from a given list
print(np.random.choice([2, 4, 6, 7]))                  # --> one of 2, 4, 6, 7
print(np.random.choice([1, 2, 3, 8], size=(3, 3)))     # --> 3x3 array of values from the list

# seed: fixes the starting state of the pseudo-random generator, so results are
# reproducible. NOTE: this also makes every random example BELOW reproducible
# when the file runs from top to bottom.
np.random.seed(42)
print(np.random.randint(1, 10, size=5))  # --> [7 4 8 5 7]
# A second call continues the sequence, so it gives different numbers.
# To repeat the first result, call np.random.seed(42) again before drawing.
print(np.random.randint(1, 10, size=5))  # --> [3 7 8 5 4]


#========================
# Random Data Distribution

# choice with p= draws values with the given probabilities (p must sum to 1)
data = np.random.choice([1, 2, 3, 4], p=[0.3, 0.2, 0.4, 0.1], size=50)
print(data)  # --> 50 values; 3 appears most often, 4 least often

# A probability of 0.0 means the value (9) is never chosen
data = np.random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(6, 6))
print(data)  # --> 6x6 array containing only 3, 5, and 7


#========================
# Random Permutations

# shuffle rearranges the ORIGINAL array in place
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)  # --> e.g. [2 4 5 1 3]

# permutation returns a rearranged COPY and leaves the original untouched
arr = np.array([1, 2, 3, 4, 5])
print(np.random.permutation(arr))  # --> e.g. [4 3 1 5 2]


#========================
# Visualizing Distributions

# Histogram: counts how often each value occurs
sns.displot([0, 1, 2, 3, 4, 5])
plt.show()

# KDE: a smooth curve estimating the distribution
sns.displot([0, 1, 2, 3, 4, 5], kind='kde')
plt.show()


#========================
# Normal Distribution

# loc = mean, scale = standard deviation, size = output shape
samples = np.random.normal(loc=1, scale=2, size=(2, 3))
print(samples)  # --> 2x3 array of values centered around 1 (std 2)

# 100 standard-normal samples form the classic bell curve
samples = np.random.normal(size=100)
sns.displot(samples, kind='kde')
plt.show()


#========================
# Binomial Distribution

# Number of successes in n trials, each succeeding with probability p
# (e.g. heads in 10 fair coin flips)
samples = np.random.binomial(n=10, p=0.5, size=10)
print(samples)  # --> 10 values between 0 and 10, e.g. [4 2 6 4 7 8 7 4 2 7]

sns.displot(np.random.binomial(n=10, p=0.5, size=1000))
plt.show()  # --> discrete bars, centered at n * p = 5

# Normal vs binomial: normal is continuous, binomial is discrete.
# With a large n the binomial curve closely resembles the normal curve.
comparison = {
    "normal": np.random.normal(loc=50, scale=5, size=1000),
    "binomial": np.random.binomial(n=100, p=0.5, size=1000),
}
sns.displot(comparison, kind="kde")
plt.show()


#========================
# Poisson Distribution

# Number of events in a fixed interval; lam = expected number of events
samples = np.random.poisson(lam=2, size=10)
print(samples)  # --> 10 small non-negative ints, e.g. [1 3 3 1 1 2 1 2 0 1]

sns.displot(np.random.poisson(lam=2, size=1000))
plt.show()

# Normal vs Poisson: with a large lam, Poisson looks like a normal curve
# (but remains discrete)
comparison = {
    "normal": np.random.normal(loc=50, scale=7, size=1000),
    "poisson": np.random.poisson(lam=50, size=1000),
}
sns.displot(comparison, kind="kde")
plt.show()

# Binomial vs Poisson: for a large n and a small p, binomial(n, p) approximates
# Poisson(lam = n * p). Here 1000 * 0.01 = 10.
comparison = {
    "binomial": np.random.binomial(n=1000, p=0.01, size=1000),
    "poisson": np.random.poisson(lam=10, size=1000),
}
sns.displot(comparison, kind="kde")
plt.show()


#========================
# Uniform Distribution

# Every value between low and high is equally likely
samples = np.random.uniform(low=0.0, high=1.0, size=(2, 3))
print(samples)  # --> 2x3 array of floats between 0 and 1

sns.displot(np.random.uniform(size=1000), kind="kde")
plt.show()  # --> roughly flat curve between 0 and 1


#========================
# Logistic Distribution

# Used in machine learning and neural networks (e.g. logistic regression).
# Similar to the normal distribution but with heavier tails.
samples = np.random.logistic(loc=1, scale=2, size=(2, 3))
print(samples)  # --> 2x3 array of values centered around 1

sns.displot(np.random.logistic(size=1000), kind="kde")
plt.show()


#========================
# Multinomial Distribution

# Generalizes the binomial distribution to more than two outcomes.
# Example: rolling a fair 6-sided die n=6 times, repeated for a (2, 3) grid.
samples = np.random.multinomial(n=6, pvals=[1/6] * 6, size=(2, 3))
print(samples)
# --> shape (2, 3, 6): each sample holds ONE count per outcome (not a single
#     value), and the six counts in every sample add up to n = 6.


#========================
# Exponential Distribution

# Models the waiting time until the next event. scale = 1 / event rate
samples = np.random.exponential(scale=2, size=(2, 3))
print(samples)  # --> 2x3 array of positive floats (average around 2)

sns.displot(np.random.exponential(size=1000), kind='kde')
plt.show()  # --> sharp peak at 0 that decays quickly


#========================
# Chi-Square Distribution

# Used in hypothesis testing. df = degrees of freedom
samples = np.random.chisquare(df=2, size=(2, 3))
print(samples)  # --> 2x3 array of positive floats

sns.displot(np.random.chisquare(df=1, size=1000), kind='kde')
plt.show()
