<div align="center">

# ⭐Statistics & Probability⭐

</div>

- 🟦 [Mean, Median, and Mode](#-mean-median-and-mode)
- 🟦 [Population Mean vs Sample Mean](#-population-mean-vs-sample-mean)
- 🟦 [Quartiles and Box Plot](#-quartiles-and-box-plot)
- 🟦 [Range and Mid-Range](#-range-and-mid-range)
- 🟦 [Variance and Standard Deviation](#-variance-and-standard-deviation)
- 🟦 [Probability](#-probability)
- 🟦 [Permutations and Combinations](#-permutations-and-combinations)
- 🟦 [Bayes' Theorem](#-bayes-theorem)
- 🟦 [Random Variables](#-random-variables)
- 🟦 [Expected Value (Expectation)](#-expected-value-expectation)
- 🟦 [Binomial Distribution](#-binomial-distribution)
- 🟦 [Poisson Distribution](#-poisson-distribution)
- 🟦 [Normal Distribution](#-normal-distribution)
- 🟦 [Central Limit Theorem (CLT)](#-central-limit-theorem-clt)
- 🟦 [Skewness and Kurtosis](#-skewness-and-kurtosis)
- 🟦 [Confidence Interval (CI)](#-confidence-interval-ci)
- 🟦 [Difference Between Z-Test and T-Test](#-difference-between-z-test-and-t-test)
- 🟦 [Degrees of Freedom (df)](#-degrees-of-freedom-df)
- 🟦 [Hypothesis Testing](#-hypothesis-testing)
- 🟦 [Mean and Variance of Difference Between Two Random Variables](#-mean-and-variance-of-difference-between-two-random-variables)
- 🟦 [Chi-Square Test (χ² Test)](#-chi-square-test-χ-test)
- 🟦 [ANOVA (Analysis of Variance)](#-anova-analysis-of-variance)
- 🟦 [Linear Regression](#-linear-regression)
- 🟦 [Covariance, Correlation, and Causation](#-covariance-correlation-and-causation)

---

<div align="center">

## 🟦 Mean, Median, and Mode

</div>

### Mean: The (average) is the sum of all values divided by the number of values. It represents the central value of a dataset.
### Median: the middle value in a dataset when the numbers are arranged in ascending order. If there are two middle values, take their average.
### Mode: the value that appears most frequently in the dataset.

**Example** using the data: `[23, 29, 20, 32, 23, 21, 33, 25]`

Sum = 206  
Number of values (n) = 8  
**Mean** = 206 / 8 = **25.75**



Sorted data: `[20, 21, 23, 23, 25, 29, 32, 33]`  
**Median** = (23 + 25) / 2 = **24**

In the data, **23** appears twice while all other values appear once.  
**Mode** = **23**

---
<div align="center">

### 🟦 Population Mean vs Sample Mean

</div>

- **Population Mean** (denoted as **ν** or usually **μ**):  
  The true average of the entire population. It is a fixed value but usually unknown because we rarely have access to the full population.

- **Sample Mean** (denoted as **x̄**):  
  The average calculated from a subset (sample) of the population. It is used to estimate the population mean.

**Key Difference**:  
The population mean (ν) describes the whole group, while the sample mean (x̄) is an estimate based on observed data. As sample size increases, the sample mean tends to get closer to the population mean (Law of Large Numbers).

---
<div align="center">

## 🟦 Quartiles and Box Plot

</div>

**Quartiles** divide an ordered dataset into four equal parts. They help understand the spread and distribution of the data.

- **Q1 (First Quartile)**: The median of the lower half of the data (25th percentile).
- **Q2 (Second Quartile)**: The median of the entire dataset (50th percentile).
- **Q3 (Third Quartile)**: The median of the upper half of the data (75th percentile).
- **IQR (Interquartile Range)**: The range between Q3 and Q1 (`IQR = Q3 - Q1`). It measures the spread of the middle 50% of the data.

### Box Plot
A box plot (box-and-whisker plot) visually represents the distribution using the five-number summary: minimum, Q1, median (Q2), Q3, and maximum. It also shows outliers.

<img src="Photos\box_plot.png" alt="Description" width="1200" height="400">

### Example
Using the dataset: `[3, 5, 7, 8, 9, 11, 13, 15]`

- Sorted data: `[3, 5, 7, 8, 9, 11, 13, 15]` (n = 8)
- **Median (Q2)** = (8 + 9) / 2 = **8.5**
- **Q1** (median of lower half `[3, 5, 7, 8]`) = (5 + 7) / 2 = **6**
- **Q3** (median of upper half `[9, 11, 13, 15]`) = (11 + 13) / 2 = **12**
- **IQR** = Q3 - Q1 = 12 - 6 = **6**

**Lower Whisker (Lower Fence)**: Q1 - 1.5 × IQR = 6 - 1.5×6 = **-3**  
**Upper Whisker (Upper Fence)**: Q3 + 1.5 × IQR = 12 + 1.5×6 = **21**

No outliers in this dataset (all values are between -3 and 21).

---

<div align="center">

## 🟦 Range and Mid-Range

</div>

### Range
The **range** is the difference between the maximum and minimum values in a dataset. It gives a basic measure of the total spread of the data.

### Mid-Range
The **mid-range** is the average of the maximum and minimum values. It provides a simple (but rough) measure of the center of the data.

### Example
Using the dataset: `[65, 81, 73, 85, 94, 79]`

- Sorted: `[65, 73, 79, 81, 85, 94]`
- **Minimum** = 65
- **Maximum** = 94
- **Range** = 94 - 65 = **29**
- **Mid-Range** = (94 + 65) / 2 = **79.5**

---

<div align="center">

## 🟦 Variance and Standard Deviation

</div>

### Variance
**Variance** measures how far each number in the dataset is from the mean (on average). It quantifies the spread of the data.

### Standard Deviation
**Standard Deviation** is the square root of the variance. It is expressed in the same units as the original data, making it easier to interpret.

### Two Formulas (Population vs Sample)

**Population Variance** (σ²):  
$σ² = Σ(xᵢ - μ)² / N$

**Population Standard Deviation** (σ):  
$σ = √σ²$

**Sample Variance** (s²):  
$s² = Σ(xᵢ - x̄)² / (n - 1)$
*(Bessel's correction — divides by n-1 to get an unbiased estimator of the population variance)*

**Sample Standard Deviation** (s):  
$s = √s²$

### Example
Using the dataset: `[20, 22, 24, 26, 28]`

- Mean (x̄) = 24

**Population Variance** (σ²):  
= [(20-24)² + (22-24)² + (24-24)² + (26-24)² + (28-24)²] / 5  
= (16 + 4 + 0 + 4 + 16) / 5 = 40 / 5 = **8**

**Population Standard Deviation** (σ) = √8 ≈ **2.83**

**Sample Variance** (s²):  
= (40) / (5 - 1) = 40 / 4 = **10**

**Sample Standard Deviation** (s) = √10 ≈ **3.16**

---

<div align="center">

## 🟦 Probability

</div>

**Probability** is a measure of the likelihood that an event will occur. It is a number between 0 and 1 (or 0% to 100%), where 0 means impossible and 1 means certain.

**Example**:  
When throwing a fair six-sided die, what is the probability of getting an even number?  

Even numbers: 2, 4, 6 (3 outcomes)  
Total possible outcomes: 6  
**P(Even)** = 3/6 = **0.5** or **1/2**

---

### Addition Rule (OR Rule)

**Mutually Exclusive Events** (events that cannot happen at the same time):  
$[ P(A \cup B) = P(A) + P(B)]$

**Non-Mutually Exclusive Events** (events that can happen at the same time):  
$[ P(A \cup B) = P(A) + P(B) - P(A \cap B)]$

**Example 1 (Dice)**:  
P(2 or 5) on a fair die  
$[ P(2 \cup 5) = \frac{1}{6} + \frac{1}{6} = \frac{1}{3}]$ (mutually exclusive)

**Example 2 (Cards)**:  
Standard deck of 52 cards.  
P(Heart or Ace)  
There are 13 Hearts and 4 Aces, but 1 Ace of Hearts is counted in both.  
$[ P(\text{Heart} \cup \text{Ace}) = \frac{13}{52} + \frac{4}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}]$

---

### Independent Events

**Law**: Two events are independent if the occurrence of one does not affect the probability of the other.  
$[ P(A \cap B) = P(A) \times P(B)]$

**Examples**:

- Throw a coin and a die: P(Heads and 3)  
  $[ P(H) \times P(3) = \frac{1}{2} \times \frac{1}{6} = \frac{1}{12}]$

- Throw a coin 3 times: P(Heads, Tails, Heads)  
  $[ P(H) \times P(T) \times P(H) = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8}]$

- Throw a coin 4 times: P(at least one Head)  
  Easier way: 1 - P(all Tails)  
  $[ P(\text{all Tails}) = \left(\frac{1}{2}\right)^4 = \frac{1}{16}]$  
  $[ P(\text{at least one Head}) = 1 - \frac{1}{16} = \frac{15}{16}]$

---

### Dependent Events

**Law**: The probability of the second event depends on the outcome of the first.  
$[ P(A \cap B) = P(A) \times P(B|A)]$  
(where $( P(B|A) )$ is the conditional probability of B given that A has occurred)

**Examples**:

1. Bag contains 5 red balls and 3 blue balls (total 8). Draw without replacement.  
   P(First Blue and Second Red)  
   $[ P(\text{Blue first}) = \frac{3}{8}]$  
   $[ P(\text{Red second} | \text{Blue first}) = \frac{5}{7}]$  
   $[ P = \frac{3}{8} \times \frac{5}{7} = \frac{15}{56}]$

2. 8 coins in a bag: 3 unfair coins (P(Heads) = 0.6), 5 fair coins (P(Heads) = 0.5).  
   You pick one coin at random and flip it twice. Find P(both Heads).  

   - $P(Pick unfair) = 3/8, P(Pick fair) = 5/8$
   - $P(HH | unfair) = 0.6 × 0.6 = 0.36$
   - $P(HH | fair) = 0.5 × 0.5 = 0.25$

   $[ P(HH) = \left(\frac{3}{8} \times 0.36\right) + \left(\frac{5}{8} \times 0.25\right) = 0.135 + 0.15625 = \mathbf{0.29125}]$

---

<div align="center">

## 🟦 Permutations and Combinations

</div>

### Permutations
**Permutations** are arrangements of items where **order matters**.

**Formula**:  
$[ P(n, r) = \frac{n!}{(n - r)!}]$

### Combinations
**Combinations** are selections of items where **order does not matter**.

**Formula**:  
$[ C(n, r) = \frac{n!}{r!(n - r)!}]$

---

### Example: 5 Persons Choosing 3 Positions
We have 5 people and want to assign 3 of them to distinct positions: **President, Minister, Server**.

- **Permutation** (order matters):  
  $[ P(5, 3) = 5 \times 4 \times 3 = \mathbf{60}]$

- **Combination** (order does not matter):  
  $[ C(5, 3) = \frac{5!}{3!(5-3)!} = 10]$

---

### Probability Using Combinations (Binomial Probability)

Many probability problems involving "exactly k successes" or "at least k" use combinations with the binomial formula:

$[ P(k) = C(n, k) \times p^k \times (1-p)^{n-k}]$

#### Example 1: Coin Flips (4 times)
Fair coin (p = 1/2)

- **P(Exactly one Head)**:  
  $[ C(4, 1) \times (0.5)^1 \times (0.5)^3 = 4 \times \frac{1}{16} = \mathbf{4/16} = \mathbf{0.25}]$

- **P(Exactly two Heads)**:  
  $[ C(4, 2) \times (0.5)^2 \times (0.5)^2 = 6 \times \frac{1}{16} = \mathbf{6/16} = \mathbf{0.375}]$

#### Example 2: Free Throws (80% success rate)
Player makes free throw with probability p = 0.8, n = 5 attempts.

- **P(Exactly 3 baskets)**:  
  $[ C(5, 3) \times (0.8)^3 \times (0.2)^2 = 10 \times 0.512 \times 0.04 = \mathbf{0.2048}]$

- **P(At least 3 baskets)** = P(3) + P(4) + P(5)  
  $P(4) = C(5,4) × (0.8)^4 × (0.2)^1 = 5 × 0.4096 × 0.2 = 0.4096$

  $P(5) = C(5,5) × (0.8)^5 × (0.2)^0 = 1 × 0.32768 = 0.32768$

  **Total** = 0.2048 + 0.4096 + 0.32768 = **0.94208** (or 94.208%)

#### Example 3: Card Game (36 cards)
Deck: 4 suits (Diamonds, Hearts, Clubs, Spades), numbers 1–9 in each suit (total 36 unique cards).

A hand consists of **9 cards**. What is the probability of getting **all four 1s** in a 9-card hand?

- Number of favorable hands: Choose all 4 ones + 5 more cards from the remaining 32 cards  
  $[ C(4,4) \times C(32,5)]$

- Total possible 9-card hands:  
  $[ C(36,9)]$

**Probability** =  $[ \frac{C(4,4) \times C(32,5)}{C(36,9)}] ≈ 0.00539$

---

<div align="center">

## 🟦 Bayes' Theorem

</div>

**Bayes' Theorem** is a fundamental result in probability theory that allows us to update the probability of an event based on new evidence. It is widely used in medical diagnosis, spam filtering, and machine learning.

### Bayes' Theorem Formula
$[ P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}]$

Where:
- $( P(A|B) )$: Posterior probability (probability of A given B)
- $( P(B|A) )$: Likelihood (probability of B given A)
- $( P(A) )$: Prior probability of A
- $( P(B) )$: Total probability of B (evidence)

### Law of Total Probability
To calculate $( P(B) )$, we often use:
$[ P(B) = P(B|A) \cdot P(A) + P(B|A^c) \cdot P(A^c) ]$
(where $( A^c )$ is the complement of A)

---

### Example 1: Rare Disease
A rare disease affects **1%** of the population.  
- If sick: Test is positive **90%** of the time (true positive).  
- If not sick: Test is positive **5%** of the time (false positive).  

If the test is positive, what is the probability the person is actually sick?

- Let $( D )$: Has disease, $( T^+ )$: Positive test  
- $( P(D) = 0.01 )$, $( P(D^c) = 0.99 )$  
- $( P(T^+|D) = 0.9 )$, $( P(T^+|D^c) = 0.05 )$

$[ P(D|T^+) = \frac{0.9 \times 0.01}{0.9 \times 0.01 + 0.05 \times 0.99} = \frac{0.009}{0.009 + 0.0495} = \frac{0.009}{0.0585} \approx \mathbf{0.1538} ]$  
**(15.38%)**

---

### Example 2: Spam Filter
10% of messages are spam.  
- "SHOW NOW" appears in **50%** of spam messages.  
- "SHOW NOW" appears in **2%** of normal messages.  

If a message contains "SHOW NOW", what is the probability it is spam?

- Let $( S )$: Spam, $( W )$: Contains "SHOW NOW"  
- $( P(S) = 0.1 )$, $( P(S^c) = 0.9 )$  
- $( P(W|S) = 0.5 )$, $( P(W|S^c) = 0.02 )$

$[ P(S|W) = \frac{0.5 \times 0.1}{0.5 \times 0.1 + 0.02 \times 0.9} = \frac{0.05}{0.05 + 0.018} = \frac{0.05}{0.068} \approx \mathbf{0.7353} ]$  
**(73.53%)**

---

### Example 3: Two Dice
There are two dice: one fair, one unfair (shows 6 with probability **50%**).  
You pick one die at random and roll a 6. What is the probability it is the unfair die?

- Let $( U )$: Unfair die, $( F )$: Fair die, $( Six )$: Rolled a 6  
- $( P(U) = P(F) = 0.5 )$  
- $( P(Six|U) = 0.5 )$, $( P(Six|F) = \frac{1}{6} )$

$[ P(U|Six) = \frac{0.5 \times 0.5}{0.5 \times 0.5 + \frac{1}{6} \times 0.5} = \frac{0.25}{0.25 + 0.0833} \approx \frac{0.25}{0.3333} = \mathbf{0.75} ]$  
**(75%)**

---

### Example 4: Fair and Unfair Coins
Bag contains **5 fair coins** and **10 unfair coins** (P(Heads) = **80%**).  
You pick one coin at random and flip it 6 times, getting **4 Heads**. What is the probability it is a fair coin?

This uses **Binomial Likelihood** with Bayes' Theorem.

- Let $( F )$: Fair coin, $( U )$: Unfair coin  
- $( P(F) = 5/15 = 1/3 )$, $( P(U) = 10/15 = 2/3 )$  
- Likelihood for fair: $( P(4H|F) = C(6,4) \times (0.5)^6 )$  
- Likelihood for unfair: $( P(4H|U) = C(6,4) \times (0.8)^4 \times (0.2)^2 )$

After calculating both likelihoods and applying Bayes' Theorem, you get the posterior probability.

--- 

<div align="center">

## 🟦 Random Variables

</div>

A **Random Variable** is a numerical outcome of a random phenomenon. It is a function that assigns a real number to each possible outcome in a sample space. Random variables allow us to use mathematical tools to analyze uncertainty and probability.

**Examples**:
- The number of heads when flipping a coin 3 times.
- The height of a randomly selected student.
- The number of customers arriving at a store in one hour.
- The temperature tomorrow in your city.

---

### Discrete vs Continuous Random Variables

#### Discrete Random Variables
A **discrete random variable** can take only a **countable** number of distinct values (usually integers).

**Characteristics**:
- Values can be listed.
- Often results from counting.

**Examples**:
- Number of heads in 5 coin flips (possible values: 0, 1, 2, 3, 4, 5)
- Number of defective items in a batch of 50 products (0, 1, 2, ..., 50)
- Roll of a fair six-sided die (1, 2, 3, 4, 5, 6)

#### Continuous Random Variables
A **continuous random variable** can take any value within a given **interval** (uncountably infinite values).

**Characteristics**:
- Values cannot be listed completely.
- Usually results from measuring.
- Probability of any exact single value is zero.

**Examples**:
- Height of a person (e.g., any value between 140 cm and 200 cm)
- Time it takes to complete a task (e.g., 12.35 seconds)
- Weight of a randomly selected apple
- Temperature in a city on a given day

---

<div align="center">

## 🟦 Expected Value (Expectation)

</div>

The **Expected Value** (denoted as **E(X)**) of a random variable is the long-run average value of repetitions of the experiment it represents. It is a weighted average of all possible outcomes, where the weights are their probabilities.

### Formula
For a discrete random variable $( X )$:

$[ E(X) = \sum [x_i \cdot P(x_i)]]$

(where the sum is over all possible values of $( X )$)

---

### Examples

#### Example 1: Rolling a Fair Die
What is the expected value of one roll of a fair six-sided die?

Possible outcomes: 1, 2, 3, 4, 5, 6 (each with probability $( \frac{1}{6} )$)

$[ E(X) = (1 \times \frac{1}{6}) + (2 \times \frac{1}{6}) + (3 \times \frac{1}{6}) + (4 \times \frac{1}{6}) + (5 \times \frac{1}{6}) + (6 \times \frac{1}{6}) = \frac{21}{6} = \mathbf{3.5}]$

---

#### Example 2: Lottery Game
You pay **$10** to participate. You have a **1%** chance to win **$1000**, otherwise you win nothing.

Let $( X )$ = net gain

- Win: $( X = 1000 - 10 = 990 )$ with probability 0.01  
- Lose: $( X = -10 )$ with probability 0.99

$[ E(X) = (990 \times 0.01) + (-10 \times 0.99) = 9.9 - 9.9 = \mathbf{0}]$

The game is **fair** (expected value = 0).

---

#### Example 3: Choosing the Best Job
- **Job 1**: Fixed salary = **$5000**

- **Job 2**: Base salary **$3000** + commission:  
  - $2000 with 50% probability  
  - $4000 with 30% probability  
  - $0 with 20% probability

**Expected Commission** for Job 2:  
$[ E(\text{Commission}) = (2000 \times 0.5) + (4000 \times 0.3) + (0 \times 0.2) = 1000 + 1200 + 0 = \mathbf{2200} ]$

**Expected Total Salary for Job 2**:  
$[ 3000 + 2200 = \mathbf{5200} ]$

**Conclusion**:  
**Job 2** is better. Its expected salary (**$5200**) is higher than Job 1 (**$5000**).

---

<div align='center'>

## 🟦 Binomial Distribution

</div>

The **Binomial Distribution** is a discrete probability distribution that describes the number of successes in a fixed number of independent Bernoulli trials (yes/no experiments), each having the same probability of success.

**Conditions for Binomial Distribution**:
- Fixed number of trials (n)
- Each trial has only two outcomes: success or failure
- Probability of success (p) is constant for each trial
- Trials are independent

<div align='center'>

<img src="Photos\binomial.png" alt="Description" width="800" height="400">

</div>

### Formula
The probability of getting exactly **k** successes in **n** trials is:

$[ P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} ]$

Where:
- $( \binom{n}{k} )$ = Combination of n things taken k at a time
- p = probability of success on a single trial

### Mean and Variance
- **Mean** (Expected Value):  
  $[ \mu = n \cdot p ]$

- **Variance**:  
  $[ \sigma^2 = n \cdot p \cdot (1-p) ]$

- **Standard Deviation**:  
  $[ \sigma = \sqrt{n \cdot p \cdot (1-p)} ]$

---

### Example
Let $( X )$ = number of heads when flipping a fair coin **5 times**.

- n = 5, p = 0.5 (fair coin)

**Find P(X = 3)** (exactly 3 heads):

$[ P(X=3) = \binom{5}{3} \times (0.5)^3 \times (0.5)^{2} = 10 \times \frac{1}{8} \times \frac{1}{4} = 10 \times \frac{1}{32} = \mathbf{\frac{10}{32}} = \mathbf{0.3125} ]$

**Mean**: $( \mu = 5 \times 0.5 = 2.5 )$ heads  
**Variance**: $( \sigma^2 = 5 \times 0.5 \times 0.5 = 1.25 )$

---

<div align='center'>

## 🟦 Poisson Distribution

</div>

The **Poisson Distribution** is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space, when these events occur with a known constant mean rate and independently of the time since the last event.

It is commonly used for modeling rare events, such as the number of calls to a call center, number of accidents, or number of customers arriving at a store.

<div align='center'>

<img src="Photos\Poisson.png" alt="Description" width="800" height="400">

</div>

### Formula
The probability of observing exactly **k** events is:

$[ P(X = k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}]$

Where:
- $( \lambda )$ = average rate of occurrence (mean number of events in the interval)
- $( e )$ ≈ 2.71828 (Euler’s number)
- $( k! )$ = factorial of k

### Mean and Variance
- **Mean** (Expected Value):  
  $[ \mu = \lambda ]$

- **Variance**:  
  $[ \sigma^2 = \lambda ]$

- **Standard Deviation**:  
  $[ \sigma = \sqrt{\lambda} ]$

---

### Example: Customer Service Center
On average, **3 calls** arrive every hour ($( \lambda = 3 )$).

#### 1. Probability of exactly 5 calls in the next hour $( \lambda = 3)$
$[ P(X=5) = \frac{e^{-3} \cdot 3^5}{5!} = \frac{e^{-3} \cdot 243}{120} \approx \mathbf{0.1008} ]$  
**(≈ 10.08%)**

#### 2. Probability of exactly 9 calls in the next two hours
In two hours, the average rate doubles: $( \lambda = 3 \times 2 = 6 )$

$[ P(X=9) = \frac{e^{-6} \cdot 6^9}{9!} \approx \mathbf{0.0688} ]$  
**(≈ 6.88%)**

---

<div align='center'>

## 🟦 Normal Distribution

</div>

The **Normal Distribution** (also called Gaussian Distribution) is one of the most important continuous probability distributions. It is symmetric and bell-shaped, and many natural phenomena (heights, test scores, measurement errors, etc.) tend to follow a normal distribution.

<div align='center'>

<img src="Photos\normal.png" alt="Description" width="800" height="400">

</div>

### Probability Density Function (PDF)
The formula for the probability density function of a normal distribution is:

$[ f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}]$

Where:
- $( \mu )$ = mean (center of the distribution)
- $( \sigma )$ = standard deviation (controls the spread)
- $( e )$ ≈ 2.71828

---

### Empirical Rule (68-95-99.7 Rule)
For any normal distribution:
- **≈ 68%** of the data falls within **1 standard deviation** of the mean $(( \mu \pm \sigma ))$
- **≈ 95%** of the data falls within **2 standard deviations** of the mean $(( \mu \pm 2\sigma ))$
- **≈ 99.7%** of the data falls within **3 standard deviations** of the mean $(( \mu \pm 3\sigma ))$

---

### Z-Score (Standard Score)
The **Z-score** tells us how many standard deviations a data point is from the mean. It allows us to compare values from different normal distributions.

$[ Z = \frac{X - \mu}{\sigma}]$

- Positive Z → above the mean
- Negative Z → below the mean

---

### Cumulative Distribution Function (CDF)
The **CDF** gives the probability that a random variable $( X )$ takes a value less than or equal to a specific value $( x )$. It represents the area under the PDF curve from negative infinity to $( x )$.

<div align='center'>

<img src="Photos\cdf.png" alt="Description" width="800" height="400">

</div>

---

### Example: Applying Normal Distribution
The heights of adult males are normally distributed with a **mean $(( \mu ))$** of 175 cm and a **standard deviation ($( \sigma )$)** of 8 cm.

1. What is the probability that a randomly selected man is taller than 191 cm?  
   Z-score = (191 - 175) / 8 = **2**  
   Using standard normal tables or calculator:  
   P(Z > 2) ≈ **0.0228** or **2.28%**

2. What is the probability that a man’s height is between 167 cm and 183 cm?  
   Z1 = (167 - 175)/8 = **-1**  
   Z2 = (183 - 175)/8 = **1**  
   P(-1 < Z < 1) ≈ **0.6827** or **68.27%** (matches the Empirical Rule)

---

<div align='center'>

## 🟦 Central Limit Theorem (CLT)

</div>

The **Central Limit Theorem** is one of the most powerful and important results in statistics. It states that:

> When you take sufficiently large independent random samples from **any** population (with finite mean and variance), the **sampling distribution of the sample means** will be approximately **normally distributed**, regardless of the shape of the original population.

### How It Works
- As the sample size (**n**) increases, the distribution of the sample means approaches a normal distribution.
- The mean of the sampling distribution equals the population mean (**μ**).
- The standard deviation of the sampling distribution (called **Standard Error**) is:  
  $[ \sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}]$

The larger the sample size (**n ≥ 30** is often considered sufficient), the closer the sampling distribution gets to normal.

---

### Uniform Distribution (Concise)
A **Uniform Distribution** is a continuous probability distribution where all outcomes in an interval are equally likely. It has a flat (rectangular) shape.

**Example**: Rolling a fair die (discrete uniform) or generating a random number between 0 and 1 (continuous uniform).

---

### Example: Converting Uniform to Normal via CLT
Suppose we have a **uniform distribution** between 0 and 1 (mean μ = 0.5, variance = 1/12).

We want to generate a distribution that is approximately normal:

1. Take **independent random samples** of size **n = 30** from the Uniform(0,1) distribution.
2. Calculate the **sample mean** ($(\bar{x})$) for each sample.
3. Repeat this process many times (e.g., 1000 times).

According to the **Central Limit Theorem**, the distribution of these sample means will be **approximately normal**, even though the original population (Uniform) is not normal.

This is a common technique in data science and simulations to approximate normal distributions from non-normal data.

---

## Example: Water Consumption (Using Central Limit Theorem)

The average male drinks **2 liters** of water when active outdoors, with a **standard deviation of 0.7 L**.  
You are planning a full-day nature trip for **50 men** and bring **110 liters** of water. What is the probability that you will run out of water?

### Solution

- Population: μ = 2 L, σ = 0.7 L  
- Sample size: n = 50 (large enough for CLT to apply)  
- Total water available: 110 L → Average per person = 110 / 50 = **2.2 L**

We need:  
**P(Total water needed > 110 L)** = **P(Sample Mean > 2.2 L)**

**Standard Error** (SE) of the mean:  
$[ SE = \frac{\sigma}{\sqrt{n}} = \frac{0.7}{\sqrt{50}} \approx \frac{0.7}{7.071} \approx 0.099]$

**Z-score**:  
$[ Z = \frac{2.2 - 2}{0.099} \approx \frac{0.2}{0.099} \approx \mathbf{2.02}]$

Using standard normal table:  
**P(Z > 2.02)** ≈ **0.0217** or **2.17%**

---

**Conclusion**: There is approximately a **2.17%** chance that you will run out of water.

---

<div align='center'>

## 🟦 Skewness and Kurtosis

</div>

### Skewness
**Skewness** measures the **asymmetry** of a probability distribution.

- **Positive Skew** (Right-skewed): The tail is longer on the right side. Most values are concentrated on the left. (Mean > Median)
- **Negative Skew** (Left-skewed): The tail is longer on the left side. Most values are concentrated on the right. (Mean < Median)
- **Zero Skew**: The distribution is symmetrical (like the Normal distribution).

<div align='center'>

<img src="Photos\skew.png" alt="Description" width="800" height="400">

</div>

### Kurtosis
**Kurtosis** measures the **tailedness** (sharpness of the peak and thickness of the tails) of a distribution compared to a normal distribution.

- **High Kurtosis** (Leptokurtic): Sharp peak and heavy tails. More outliers.
- **Low Kurtosis** (Platykurtic): Flatter peak and lighter tails.
- **Mesokurtic** (Kurtosis ≈ 3): Similar to the normal distribution.

<div align='center'>

<img src="Photos\kurtosis.png" alt="Description" width="800" height="400">

</div>

---

<div align='center'>

## 🟦 Confidence Interval (CI)

</div>

A **Confidence Interval** is a range of values used to estimate an unknown population parameter (such as the mean or proportion). It gives an interval that is likely to contain the true population value with a certain level of confidence (e.g., 95%).

### Formula (for Population Mean)
When sample size is large (n ≥ 30):

$[ \bar{x} \pm z \cdot \frac{s}{\sqrt{n}}]$

Where:
- $( \bar{x})$ = sample mean
- $( s )$ = sample standard deviation
- $( n )$ = sample size
- $( z )$ = critical value (1.96 for 95% confidence)

---

### Example 1: Student Grades
A school has 500 students. You sampled **36 students** and found:
- Sample mean ($( \bar{x} )$) = **70**
- Sample standard deviation (s) = **12**

Find the **95% Confidence Interval** for the population mean.

**Standard Error**:
$[ SE = \frac{12}{\sqrt{36}} = \frac{12}{6} = 2]$

**Margin of Error**:
$[ 1.96 \times 2 = 3.92 ]$

**95% CI**:
$[ 70 \pm 3.92 = (66.08, 73.92)]$

**Interpretation**: We are 95% confident that the true average grade of all 500 students lies between **66.08** and **73.92**.

---

## Bernoulli Distribution

The **Bernoulli Distribution** is the simplest discrete probability distribution. It describes a single trial with only two possible outcomes: success (1) with probability **p**, or failure (0) with probability **1-p**.

- **Mean** (μ) = **p**
- **Variance** = $p(1-p)$
- **Standard Deviation** = $√[p(1-p)]$

---

### Example 2: Confidence Interval for Proportion
In a survey, **40 out of 100** persons agreed on a decision. Find the **95% Confidence Interval** for the true population proportion.

- Sample proportion ($( \hat{p} )$) = 40/100 = **0.40**
- n = 100

**Standard Error**:
$[ SE = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} = \sqrt{\frac{0.4 \times 0.6}{100}} = \sqrt{0.0024} \approx 0.049]$

**Margin of Error**:
$[ 1.96 \times 0.049 \approx 0.096]$

**95% CI**:
$[ 0.40 \pm 0.096 = (0.304, 0.496) ]$ or **(30.4%, 49.6%)**

**Interpretation**: We are 95% confident that the true proportion of people who agree in the population is between **30.4%** and **49.6%**.

---

<div align='center'>

## 🟦 Difference Between Z-Test and T-Test

</div>

| Aspect                  | Z-Test                                      | T-Test                                          |
|-------------------------|---------------------------------------------|-------------------------------------------------|
| **Population SD**       | Known (σ)                                   | Unknown (use sample SD 's')                     |
| **Sample Size**         | Large (n ≥ 30)                              | Small (n < 30)                                  |
| **Distribution**        | Normal                                      | t-distribution (heavier tails)                  |
| **When to Use**         | Large samples, σ known                      | Small samples, σ unknown                        |
| **Formula**             | Uses σ in denominator                       | Uses s in denominator                           |
| **Degrees of Freedom**  | Not applicable                              | n - 1                                           |
| **Sensitivity**         | Less sensitive to outliers                  | More sensitive to outliers                      |


### [Z-Table](https://media.cheggcdn.com/media/24e/24ef20f3-7ce3-4063-8fd8-27b1770c4331/phpTBlQEv.png)

### [t-table](https://www.scribbr.com/wp-content/uploads/2022/06/Critical-values-of-t-for-one-tailed-tests-l.webp)
---

<div align='center'>

## 🟦 Degrees of Freedom (df)

</div>

**Degrees of Freedom** represent the number of independent values that can vary in a statistical calculation.

- When estimating the **sample variance** or using the **t-distribution**, we lose one degree of freedom because the sample mean is calculated from the data first.
- **Formula**: df = n - 1 (for a single sample)

**Example**:  
For a sample of 25 students:  
**Degrees of Freedom = 25 - 1 = 24**

Degrees of freedom are especially important when using the **t-test**, as they determine the shape of the t-distribution (smaller df = wider tails).

---

<div align='center'>

##  🟦 Hypothesis Testing

</div>

**Hypothesis Testing** is a formal statistical procedure used to make decisions or draw conclusions about a population based on sample data. It helps us determine whether there is enough evidence to support a claim (hypothesis) or not.

Think of it as a **court trial**:
- We start with a presumption of innocence (Null Hypothesis).
- We collect evidence (sample data).
- We decide whether the evidence is strong enough to reject the presumption.

---

### 1. Null Hypothesis (H₀)
The **Null Hypothesis** is the default assumption or "status quo". It represents **no effect**, **no difference**, or **no change**.

- It is what we assume to be true unless proven otherwise.
- We try to find evidence **against** it.

**Example**:  
H₀: The average height of male students is 175 cm.

---

### 2. Alternative Hypothesis (H₁ or Hₐ)
The **Alternative Hypothesis** is the claim we are trying to prove. It represents the opposite of the null hypothesis.

- It can be **one-sided** (greater than or less than) or **two-sided** (not equal to).

**Example**:  
H₁: The average height of male students is **not equal** to 175 cm.

---

### 3. Significance Level (α)
The **significance level (α)** is the probability of rejecting the null hypothesis when it is actually true (Type I Error). 

- Common values: **0.05** (5%), **0.01** (1%), or **0.10** (10%).
- α = 0.05 means we are willing to accept a 5% risk of wrongly rejecting H₀.

---

### 4. One-Tailed vs Two-Tailed Tests

- **Two-Tailed Test**: Used when the alternative hypothesis says "**not equal to**". The rejection area is split on both tails of the distribution.  
  (Example: H₁: μ ≠ 175)

- **One-Tailed Test**: Used when the alternative hypothesis is directional (**greater than** or **less than**). The rejection area is only on one side.  
  - Right-tailed: H₁: μ > 175  
  - Left-tailed: H₁: μ < 175

---

### 5. Decision Making: Two Main Approaches

#### A. Critical Value Approach
1. Choose α and determine the critical value(s) from the Z or t table.
2. Calculate the test statistic (Z or t).
3. If the test statistic falls in the **rejection region**, reject H₀. Otherwise, fail to reject H₀.

#### B. P-Value Approach (Most Common Today)
- The **p-value** is the probability of getting a test statistic as extreme as (or more extreme than) the one observed, **assuming H₀ is true**.
- Decision Rule:
  - If **p-value < α** → Reject H₀ (evidence is strong)
  - If **p-value ≥ α** → Fail to reject H₀

---

### Full Example: Hypothesis Testing

A company claims that the average battery life of their smartphones is **8 hours**.  
A researcher suspects it is **different** from 8 hours.  

They test 36 phones and find:  
- Sample mean = 7.5 hours  
- Population standard deviation = 1.2 hours  

**Step-by-step:**

1. **Hypotheses**:  
   H₀: μ = 8 hours (the claim is true)  
   H₁: μ ≠ 8 hours (two-tailed test)

2. **Significance Level**: α = 0.05

3. **Test Statistic (Z-test)**:  
   $[ Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} = \frac{7.5 - 8}{1.2 / \sqrt{36}} = \frac{-0.5}{0.2} = \mathbf{-2.5}]$

4. **Critical Value Approach** (Two-tailed, α=0.05):  
   Critical values = ±1.96  
   Since -2.5 < -1.96 → **Reject H₀**

5. **P-Value Approach**:  
   P(Z ≤ -2.5) ≈ 0.0062  
   Two-tailed p-value = 2 × 0.0062 = **0.0124**  
   Since 0.0124 < 0.05 → **Reject H₀**

**Conclusion**: At 5% significance level, there is sufficient evidence to reject the company's claim. The average battery life is significantly different from 8 hours.

---

### One-Tailed T-Test (Small Sample)

A teacher believes that her students’ performance is **above** the general average mark of **80**. She takes a small sample of **16 students** and finds:

- Sample mean ($( \bar{x} )$) = **82**
- Sample standard deviation (s) = **5**
- n = 16

**Test** at 5% significance level whether the students’ marks are significantly higher than 80.

---

**Step-by-step Solution:**

1. **Hypotheses** (One-tailed test):  
   H₀: μ ≤ 80 (no improvement / not above average)  
   H₁: μ > 80 (students perform above average)

2. **Significance Level**: α = 0.05

3. **Test Used**: One-sample **t-test** (small sample + unknown population SD)

4. **Test Statistic**:
   $[ t = \frac{\bar{x} - \mu}{s / \sqrt{n}} = \frac{82 - 80}{5 / \sqrt{16}} = \frac{2}{5/4} = \frac{2}{1.25} = \mathbf{1.6} ]$

5. **Degrees of Freedom**:  
   df = n - 1 = 16 - 1 = **15**

6. **Critical Value Approach**:  
   For right-tailed test, α = 0.05, df = 15 → Critical t-value ≈ **1.753**  
   Since calculated t = **1.6** < 1.753 → **Fail to reject H₀**

7. **P-Value Approach**:  
   p-value for t=1.6 with df=15 (right tail) ≈ **0.064**  
   Since 0.064 > 0.05 → **Fail to reject H₀**

**Conclusion**: At the 5% significance level, there is **not enough evidence** to conclude that the students’ average mark is significantly above 80.

---

<div align='center'>

## 🟦 Mean and Variance of Difference Between Two Random Variables

</div>

Let $( X )$ and $( Y )$ be two independent random variables (e.g., weight loss from two different groups).

### For the Difference $( X - Y )$:

- **Mean (Expected Value)** of the difference:  
  $[ \mu_{X-Y} = \mu_X - \mu_Y ]$
  (or $( \nu_X - \nu_Y )$ for population means)

- **Variance** of the difference (for independent samples):  
  $[ \sigma^2_{X-Y} = \sigma^2_X + \sigma^2_Y ]$

- **Standard Deviation** of the difference:  
  $[ \sigma_{X-Y} = \sqrt{\sigma^2_X + \sigma^2_Y} ]$

When working with **sample data**, we use sample means ($( \bar{x}, \bar{y} )$) and sample variances ($( s^2_X, s^2_Y )$) to estimate the above.

---

### Example: Low-Fat Diet Study

A researcher wants to test whether a low-fat diet helps obese people lose more weight.

- **Group 1** (Low-fat diet): n₁ = 100, mean weight loss $( \bar{x}_1 = 9.31 )$ lbs, s₁ = 4.67  
- **Group 2** (Normal diet): n₂ = 100, mean weight loss $( \bar{x}_2 = 7.4 )$ lbs, s₂ = 4.04

#### 1. Mean and Variance of the Difference

**Mean difference** (Point estimate):  
$[ \bar{x}_1 - \bar{x}_2 = 9.31 - 7.4 = \mathbf{1.91} ]$ lbs

**Variance of the difference**:  
$[ s^2_{diff} = s_1^2 + s_2^2 = (4.67)^2 + (4.04)^2 = 21.8089 + 16.3216 = \mathbf{38.1305} ]$

**Standard Error** of the difference:  
$[ SE = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}} = \sqrt{\frac{38.1305}{100}} = \sqrt{0.381305} \approx \mathbf{0.6175} ]$

---

#### 2. 95% Confidence Interval for the Difference in Means

Since n₁ and n₂ are large (≥ 30), we use **Z-distribution** (critical value = 1.96):

**95% CI** =  
$[ (\bar{x}_1 - \bar{x}_2) \pm 1.96 \times SE = 1.91 \pm 1.96 \times 0.6175 ]$  
$[ 1.91 \pm 1.2103 = \mathbf{(0.6997, 3.1203)} ]$

**Interpretation**: We are 95% confident that the true mean difference in weight loss (low-fat diet minus normal diet) is between **0.70 lbs** and **3.12 lbs**.

---

#### 3. Hypothesis Test at α = 0.05

**Hypotheses**:  
$H₀: μ₁ - μ₂ = 0$ (no difference between diets)  
$H₁: μ₁ - μ₂ ≠ 0$ (there is a difference) — Two-tailed test

**Test Statistic (Z)**:  
$[ Z = \frac{(\bar{x}_1 - \bar{x}_2) - 0}{SE} = \frac{1.91}{0.6175} \approx \mathbf{3.093}]$

**Decision**:  
Since |Z| = 3.093 > 1.96 (critical value for α=0.05), we **reject H₀**.

**Conclusion**: At the 5% significance level, there is **statistically significant evidence** that the low-fat diet leads to greater weight loss than the normal diet (by about 1.91 lbs on average).

---

<div align='center'>

## 🟦 Chi-Square Test (χ² Test)

</div>

The **Chi-Square Test** is a statistical test used to determine whether there is a significant relationship between **categorical variables** or whether observed data fits an expected distribution. It compares **observed frequencies** with **expected frequencies**.

---

### 1. Chi-Square Test for Independence (Test of Association)

This test checks whether two categorical variables are **independent** (no relationship) or **dependent** (there is a relationship).

**Formula**:
$[ \chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}]$

Where:
- $( E_i )$ = Expected frequency
- $( O_i )$ = Observed frequency

**Degrees of Freedom**:  
$[ df = (r-1)(c-1) ]$  
(r = number of rows, c = number of columns)

---

### 2. Chi-Square Goodness of Fit Test

This test checks whether the observed data **fits** a specific expected distribution (e.g., uniform, normal, etc.).

**Formula**: Same as above  
$[ \chi^2 = \sum \frac{(O_i - E_i)^2}{E_i} ]$

**Degrees of Freedom**:  
$[ df = k - 1 ]$  
(k = number of categories)

---

### Decision Rule (α = 0.05)
- If **χ² calculated > χ² critical** (from Chi-Square table) → Reject H₀
- Or if **p-value < α** → Reject H₀


[Chi Square](https://cdn.scribbr.com/wp-content/uploads/2022/05/chi-square-distribution-table.png)
---

### Example 1: Chi-Square Test for Independence

**Data**: Food preference by gender

|          | Pizza | Burger | Total |
|----------|-------|--------|-------|
| **Men**  | 50    | 30     | 80    |
| **Women**| 40    | 20     | 60    |
| **Total**| 90    | 50     | 140   |

**Hypotheses**:  
H₀: Food preference is **independent** of gender  
H₁: Food preference is **dependent** on gender  

**Expected Frequencies** (E = (Row Total × Column Total) / Grand Total):

- Men-Pizza: (80 × 90)/140 ≈ **51.43**  
- Men-Burger: (80 × 50)/140 ≈ **28.57**  
- Women-Pizza: (60 × 90)/140 ≈ **38.57**  
- Women-Burger: (60 × 50)/140 ≈ **21.43**

**χ² Calculation**:
$[ \chi^2 = \frac{(50-51.43)^2}{51.43} + \frac{(30-28.57)^2}{28.57} + \frac{(40-38.57)^2}{38.57} + \frac{(20-21.43)^2}{21.43} \approx 0.20 ]$

**Degrees of Freedom**: (2-1)(2-1) = **1**  
**Critical Value** (α=0.05, df=1) = **3.841**

Since 0.20 < 3.841 → **Fail to reject H₀**

**Conclusion**: There is **no significant relationship** between gender and food preference at α = 0.05.

---

### Example 2: Chi-Square Goodness of Fit Test

A die is thrown **60 times**. Observed results:  
1: 8, 2: 12, 3: 9, 4: 11, 5: 10, 6: 10

**Hypotheses**:  
H₀: The die is fair (follows uniform distribution)  
H₁: The die is not fair

**Expected Frequency** for each face (fair die): 60 / 6 = **10**

**χ² Calculation**:
$[ \chi^2 = \frac{(8-10)^2}{10} + \frac{(12-10)^2}{10} + \frac{(9-10)^2}{10} + \frac{(11-10)^2}{10} + \frac{(10-10)^2}{10} + \frac{(10-10)^2}{10} ]$  
$[ = 0.4 + 0.4 + 0.1 + 0.1 + 0 + 0 = \mathbf{1.0} ]$

**Degrees of Freedom**: 6 - 1 = **5**  
**Critical Value** $(α=0.05, df=5)$ ≈ **11.070**

Since 1.0 < 11.070 → **Fail to reject H₀**

**Conclusion**: At α = 0.05, there is **not enough evidence** to say the die is unfair. The data is consistent with a fair die.

---
<div align='center'>

## 🟦 ANOVA (Analysis of Variance)

</div>

**ANOVA** is a statistical method used to test whether there are significant differences between the **means of three or more independent groups**. It helps determine if at least one group mean is different from the others.

- **One-Way ANOVA**: Used when comparing means across one factor (e.g., different teaching methods, different diets, etc.).

### Key Components of ANOVA

#### 1. Sum of Squares
- **SST (Total Sum of Squares)**: Measures the **total variability** in the data.  
  $[ SST = SSB + SSW ]$

- **SSB (Sum of Squares Between Groups)**: Measures the variability **between** the group means (explained variation).  
  It shows how different the group means are from the overall mean.

- **SSW (Sum of Squares Within Groups)**: Measures the variability **within** each group (unexplained / random variation).

#### 2. Degrees of Freedom (df)
- **df Between** (dfB): $( k - 1 )$  
  (where $( k )$ = number of groups)
- **df Within** (dfW): \( N - k \)  
  (where $( N )$ = total number of observations)
- **df Total** (dfT): $( N - 1 )$

#### 3. Mean Squares
- **MSB** (Mean Square Between) = $SSB / dfB$
- **MSW** (Mean Square Within) = $SSW / dfW$

#### 4. F-Statistic
The test statistic in ANOVA is the **F-ratio**:

$[ F = \frac{MSB}{MSW}]$

- A large F-value suggests that the variation **between** groups is much larger than the variation **within** groups → likely significant difference.
- Compare the calculated F with the critical F-value from the F-table (using dfB and dfW), or check the p-value.

**Decision Rule** (α = 0.05):  
If F calculated > F critical → Reject H₀ (there is a significant difference between at least two group means).

---

### Example: Comparing Teaching Methods

A school wants to compare the effectiveness of three teaching methods. The final exam scores of randomly selected students are shown below:

| Method A | Method B | Method C |
|----------|----------|----------|
| 78       | 85       | 92       |
| 82       | 79       | 88       |
| 75       | 83       | 95       |
| 80       | 81       | 90       |
| 85       | 84       | 93       |

- n₁ = n₂ = n₃ = 5, Total N = 15, k = 3 groups

**Step-by-step ANOVA**:

1. **Group Means**:  
   A: 80, B: 82.4, C: 91.6  
   **Grand Mean**: 84.67

2. **SSB (Between)** ≈ **378.93**  
   **dfB** = 3 - 1 = **2**  
   **MSB** = 378.93 / 2 ≈ **189.465**

3. **SSW (Within)** ≈ **148.80**  
   **dfW** = 15 - 3 = **12**  
   **MSW** = 148.80 / 12 ≈ **12.40**

4. **F-Statistic**:  
   $[ F = \frac{189.465}{12.40} \approx \mathbf{15.28}]$

5. **Critical Value**: F(2, 12) at α=0.05 ≈ **3.885**  

**Conclusion**: Since 15.28 > 3.885, we **reject H₀**.  
There is a statistically significant difference in exam scores among the three teaching methods at α = 0.05.

---

<div align='center'>

## 🟦 Linear Regression

</div>

**Linear Regression** is a statistical method used to model the relationship between a **dependent variable** (target/outcome) and one or more **independent variables** (predictors).

The goal is to find the **best-fitting straight line** that describes how the dependent variable changes as the independent variable changes.

<div align='center'>

<img src="Linear-Regression.jpg" alt="Description" width="1200" height="400">

</div>

### Simple Linear Regression
The equation of the line is:

$[ y = \beta_0 + \beta_1 x + \epsilon]$

Where:
- $( y )$ = Dependent variable (what we want to predict)
- $( x )$ = Independent variable (predictor)
- $( \beta_0 )$ = Intercept (value of y when x = 0)
- $( \beta_1 )$ = Slope (how much y changes when x increases by 1)
- $( \epsilon )$ = Error term (random noise)

---

### R² (Coefficient of Determination)

**R²** tells us **how well** the regression line fits the data. It represents the proportion of the variance in the dependent variable that is predictable from the independent variable(s).

- R² ranges from **0 to 1** (or 0% to 100%).
- **R² = 0**: The model explains none of the variability.
- **R² = 1**: The model explains all the variability (perfect fit).
- **Higher R²** = Better model fit.

**Interpretation**:  
An R² of 0.85 means that **85%** of the variation in the dependent variable can be explained by the independent variable(s).

---

### Sum of Squared Errors (SSE)

**Sum of Squared Errors (SSE)**, also called **Residual Sum of Squares**, measures the **total error** between the actual observed values and the predicted values from the regression line.

$[ SSE = \sum (y_i - \hat{y}_i)^2 ]$

Where:
- $( y_i )$ = Actual observed value
- $( \hat{y}_i )$ = Predicted value from the regression model

**Key Points**:
- Lower SSE = Better model (smaller prediction errors)
- SSE is used to calculate the Mean Squared Error (MSE) and is the foundation for many regression evaluation metrics.
- The regression line is chosen to **minimize** the SSE (this is called the Least Squares method).

---

**Relationship between SSE, SST, and R²**:

$[ R^2 = 1 - \frac{SSE}{SST} ]$

Where SST is the Total Sum of Squares (total variation in the data).


---

<div align='center'>

## 🟦 Covariance, Correlation, and Causation

</div>

### 1. Covariance
**Covariance** measures the **direction** of the linear relationship between two variables. It tells us whether two variables tend to increase or decrease together.

- **Positive Covariance**: When one variable increases, the other tends to increase.
- **Negative Covariance**: When one variable increases, the other tends to decrease.
- **Zero Covariance**: No linear relationship between the variables.

**Formula** (for sample):
$[ \text{Cov}(X, Y) = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{n-1} ]$

**Limitation**: Covariance is hard to interpret because its value depends on the units and scale of the variables. A large covariance doesn’t necessarily mean a strong relationship.

$Var(X−Y)=Var(X)+Var(Y)−2Cov(X,Y)$

$Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)$

$Cov(X,X) = Var(X)$ 

---

### 2. Correlation (Pearson Correlation Coefficient)

**Correlation** is a standardized version of covariance. It measures both the **direction** and **strength** of the linear relationship between two variables. It is always between **-1 and +1**.

- **+1**: Perfect positive linear relationship
- **-1**: Perfect negative linear relationship
- **0**: No linear relationship

**Formula**:
$[ r = \frac{\text{Cov}(X, Y)}{s_X \cdot s_Y} ]$

Where $( s_X )$ and $( s_Y )$ are the standard deviations of X and Y.

**Interpretation**:
- |r| > 0.7 → Strong correlation
- 0.3 < |r| < 0.7 → Moderate correlation
- |r| < 0.3 → Weak correlation

---

### 3. Causation

**Causation** means that one variable **directly causes** a change in another variable.

**Important Rule**:
> **Correlation does NOT imply Causation.**

Just because two variables are strongly correlated does not mean one causes the other. There may be:
- A third variable (confounding variable) affecting both.
- Pure coincidence (spurious correlation).
- Reverse causation.

**Example**:
- Ice cream sales and drowning incidents are highly correlated in summer.
- **Correlation**: Yes
- **Causation**: No — Both are caused by hot weather (third variable).

**To prove causation**, you typically need:
- Strong correlation
- Proper experimental design (e.g., Randomized Controlled Trials)
- Temporal order (cause happens before effect)
- Rule out alternative explanations

---

**Summary**:
- **Covariance** → Direction only (hard to interpret)
- **Correlation** → Direction + Strength (easy to interpret)
- **Causation** → One variable actually causes the other (much harder to prove)