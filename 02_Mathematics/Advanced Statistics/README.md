<div align='center'>

# ⭐ Advanced Statistics ⭐

</div>

## Table of Contents
- [🟦 Spearman's Rank Correlation](#-spearmans-rank-correlation)
- [🟦 Kendall's Tau](#-kendalls-tau)
- [🟦 Kolmogorov-Smirnov Test](#-kolmogorov-smirnov-test)
- [🟦 Partial Correlation](#-partial-correlation)
- [🟦 Correlation Networks](#-correlation-networks)
- [🟦 Structural Equation Modeling](#-structural-equation-modeling-sem)
- [🟦 Path Diagrams](#-path-diagrams)
- [🟦 Simpson's Paradox](#-simpsons-paradox)
- [🟦 Homoscedasticity and Normality in Linear Regression](#-homoscedasticity-and-normality-in-linear-regression)
- [🟦 A/B Testing, Causal Inference, and Difference-in-Differences (DID)](#-ab-testing-causal-inference-and-difference-in-differences-did)
- [🟦 ANCOVA and MANOVA](#-ancova-and-manova)
- [🟦 Monte Carlo Simulation](#-monte-carlo-simulation)
- [🟦 Linear Programming](#-linear-programming)

<div align='center'>

## 🟦 Spearman's Rank Correlation

</div>

### Explanation
**Spearman's rank correlation coefficient** ($\rho$ or $r_s$) measures the strength and direction of the **monotonic relationship** between two ranked variables. It is a non-parametric measure and is based on the ranks of the data rather than raw values.

**Formula:**
$$
r_s = 1 - \frac{6 \sum d_i^2}{n(n^2 - 1)}
$$
where $d_i$ is the difference between the ranks of the paired observations, and $n$ is the number of observations.

**Interpretation:**
- $+1$: Perfect positive monotonic relationship
- $-1$: Perfect negative monotonic relationship
- $0$: No monotonic relationship

### Example
Data: Study hours and exam scores

| Student | Hours (X) | Score (Y) | Rank_X | Rank_Y | $d_i$ | $d_i^2$ |
|---------|-----------|-----------|--------|--------|-------|---------|
| A       | 2         | 50        | 1      | 1      | 0     | 0       |
| B       | 4         | 65        | 2      | 2      | 0     | 0       |
| C       | 5         | 80        | 3      | 4      | -1    | 1       |
| D       | 7         | 75        | 4      | 3      | 1     | 1       |
| E       | 8         | 90        | 5      | 5      | 0     | 0       |

$n = 5$, $\sum d_i^2 = 2$

$$
r_s = 1 - \frac{6 \times 2}{5(25 - 1)} = 1 - 0.1 = 0.9
$$

**Conclusion:** Strong positive monotonic relationship.

---

<div align='center'>

## 🟦 Kendall's Tau

</div>

### Explanation
**Kendall's Tau** ($\tau$) is a non-parametric rank correlation coefficient that measures the ordinal association between two variables by counting **concordant** and **discordant** pairs.

**Formula:**
$$
\tau = \frac{C - D}{\frac{n(n-1)}{2}}
$$
where $C$ = number of concordant pairs, $D$ = number of discordant pairs.

### Example
Using the same data as above:

Total pairs = 10  
Concordant pairs ($C$) = 9  
Discordant pairs ($D$) = 1

$$
\tau = \frac{9 - 1}{10} = 0.8
$$

**Conclusion:** Strong positive rank correlation.

---

<div align='center'>

## 🟦 Kolmogorov-Smirnov Test (KS Test)

</div>

### Explanation
The **Kolmogorov-Smirnov test** is a non-parametric goodness-of-fit test that compares the empirical cumulative distribution function (ECDF) of a sample with a reference distribution (one-sample) or with another sample (two-sample).

**Test Statistic:**
$$
D = \sup_x |F_n(x) - F(x)|
$$
where $F_n(x)$ is the sample ECDF and $F(x)$ is the reference CDF.

**Hypothesis:**
- $H_0$: The data follows the specified distribution
- $H_1$: The data does not follow the specified distribution

### Example (One-Sample KS Test)
Sample: `[2.1, 2.3, 2.8, 3.1, 3.5]`  
Test if it comes from Normal distribution $\mathcal{N}(3, 0.5)$.

In practice, use software (e.g., Python's `scipy.stats.kstest`).  
Suppose the computed $D = 0.18$ and the critical value at $\alpha = 0.05$ is ~0.41.  

Since $D < $ critical value, we **fail to reject** $H_0$ — the sample is consistent with the Normal distribution.

---

<div align='center'>

## 🟦 Partial Correlation

</div>

### Explanation
**Partial correlation** measures the relationship between two variables while **controlling for the effect** of one or more other variables (called control variables). It helps isolate the direct relationship between the two primary variables by removing the influence of the confounding variables.

**Formula (for three variables):**  
The partial correlation between $X$ and $Y$ while controlling for $Z$ is:

$$
r_{XY.Z} = \frac{r_{XY} - r_{XZ} r_{YZ}}{\sqrt{(1 - r_{XZ}^2)(1 - r_{YZ}^2)}}
$$

where $r_{XY}$, $r_{XZ}$, and $r_{YZ}$ are the pairwise Pearson correlation coefficients.

### Difference Between Partial Correlation and (Regular) Correlation
- **Regular Correlation** (e.g., Pearson’s $r$): Measures the total linear relationship between two variables **without considering** any other variables. It can be misleading if there are confounding factors.
- **Partial Correlation**: Measures the relationship between two variables **after removing** the effect of other variables. It gives a clearer picture of the **direct association**.

**Example Scenario:**
- Regular correlation between “Ice cream sales” and “Drowning incidents” might be high (positive).
- Partial correlation (controlling for “Temperature”) would likely drop close to zero — showing that temperature is the confounding variable.

### Simple Example
Suppose we have three variables: Study Hours ($X$), Exam Score ($Y$), and Sleep Hours ($Z$).

- Regular correlation $r_{XY} = 0.75$
- Partial correlation $r_{XY.Z} = 0.45$

**Interpretation:**  
There is still a positive relationship between study hours and exam score, but part of it was explained by sleep hours. The direct relationship is moderate (0.45).

---

<div align='center'>

## 🟦 Correlation Networks

</div>

### Explanation
A **correlation network** is a graphical representation of the relationships between multiple variables, where each variable is a **node** and the strength of the correlation between them is represented by **edges** (lines). 

Edges are often drawn only if the correlation exceeds a certain threshold (e.g., |r| > 0.3) to reduce noise. Correlation networks are widely used in fields like biology, psychology, finance, and social sciences to visualize complex interrelationships.

**Key Features:**
- Positive correlations → solid or green edges
- Negative correlations → dashed or red edges
- Thickness of edge often represents strength of correlation
- Can be weighted or unweighted

### Example
In a study of student performance, variables include: Study Hours, Sleep Quality, Anxiety Level, Exam Score, and Attendance.

The network might show:
- Strong positive edge between Study Hours and Exam Score
- Negative edge between Anxiety Level and Exam Score
- Cluster of highly connected academic variables

These networks help identify central variables and communities (clusters) of related variables.

---

<div align='center'>

## 🟦 Structural Equation Modeling (SEM)

</div>

### Explanation
**Structural Equation Modeling (SEM)** is an advanced multivariate statistical technique that combines **factor analysis** (measurement model) and **regression/path analysis** (structural model). 

SEM is used to test complex theoretical models involving both **observed** (measured) and **latent** (unobserved) variables. It allows researchers to evaluate direct effects, indirect effects, and overall model fit.

**Main Components:**
- **Measurement Model**: Links latent variables to their observed indicators
- **Structural Model**: Shows hypothesized causal relationships between variables
- **Fit Indices**: Chi-square, CFI, TLI, RMSEA, etc.

SEM is particularly powerful because it accounts for measurement error and can model mediation and moderation effects.

### Example
A researcher wants to study how "Socioeconomic Status" (latent) affects "Academic Achievement" (latent) through "Motivation" (mediator).

SEM can test:
- Direct effect of SES on Achievement
- Indirect effect via Motivation
- Overall model fit to the data

---

<div align='center'>

## 🟦 Path Diagrams

</div>

### Explanation
**Path diagrams** are visual representations used primarily in **Structural Equation Modeling (SEM)** and path analysis to illustrate hypothesized relationships among variables.

**Common Symbols:**
- **Rectangles / Boxes**: Observed (measured) variables
- **Circles / Ovals**: Latent (unobserved) variables
- **Single-headed arrows** (→): Direct causal effects / regression paths
- **Double-headed arrows** (↔): Correlations / covariances
- **Curved arrows**: Error terms or disturbances

Path diagrams make complex models easy to understand and communicate.

---

<div align='center'>

## 🟦 Simpson's Paradox

</div>

### Explanation
**Simpson's Paradox** (also known as the Yule-Simpson effect) is a statistical phenomenon in which a trend appears in several groups of data but disappears or reverses when these groups are combined.

It occurs when a **confounding variable** (a lurking variable) influences the relationship between two other variables. This paradox highlights the importance of careful data analysis and the dangers of ignoring subgroups when interpreting correlations or trends.

**Key Insight:**  
Aggregated data can show one pattern, while the same data broken down by groups shows the opposite pattern.

### Classic Example: University Admission Rates

Suppose we have admission data from two departments:

**Department A (Engineering):**
- Males: 30 admitted out of 40 (75%)
- Females: 10 admitted out of 15 (66.7%)

**Department B (Social Sciences):**
- Males: 10 admitted out of 30 (33.3%)
- Females: 25 admitted out of 40 (62.5%)

**Overall (Combined):**
- Males: 40 admitted out of 70 (57.1%)
- Females: 35 admitted out of 55 (63.6%)

**Observation:**
- In each department, males had a **higher** acceptance rate.
- Overall, females had a **higher** acceptance rate.

**Why it happens:**  
More males applied to the highly competitive Engineering department, while more females applied to the less competitive Social Sciences department. The confounding variable (department choice) reverses the overall trend.

### Interpretation and Importance
- Always check for confounding variables when analyzing data.
- Simpson's Paradox appears in many real-world fields: medicine, economics, sports, and social sciences.
- It demonstrates why **stratified analysis** (analyzing subgroups separately) is often necessary.

**Moral:** Correlation or trends in aggregated data can be misleading. Always examine the data at the appropriate level of detail.

---

<div align='center'>

## 🟦 Homoscedasticity and Normality in Linear Regression

</div>

### Homoscedasticity

**Explanation:**  
**Homoscedasticity** (also called homogeneity of variance) assumes that the variance of the residuals (errors) is constant across all levels of the independent variable(s). In other words, the spread of the residuals should be roughly the same for all predicted values.

**Why we care:**  
- It is one of the core assumptions of Ordinary Least Squares (OLS) linear regression.  
- If violated (**heteroscedasticity**), the regression coefficients remain unbiased, but the **standard errors** become unreliable. This leads to incorrect p-values, confidence intervals, and hypothesis tests.  
- Predictions may still be okay, but statistical inference becomes invalid.

**How to check:**  
- Residuals vs. Fitted values plot (should show random scatter with no pattern).  
- Breusch-Pagan test or White test.

---

### Normality of Residuals

**Explanation:**  
The **normality assumption** states that the residuals (errors) of the model should be approximately normally distributed.

**Why we care:**  
- Normality is important for valid statistical inference (confidence intervals, t-tests, F-tests, and p-values).  
- While the Central Limit Theorem helps with large samples, serious violations in small-to-moderate samples can lead to misleading conclusions.  
- It affects the reliability of prediction intervals more than the point estimates themselves.

**How to check:**  
- Histogram or Q-Q plot of residuals.  
- Shapiro-Wilk test or Kolmogorov-Smirnov test.

---

### Summary: Why These Assumptions Matter
Violating homoscedasticity or normality doesn't necessarily make the model useless for prediction, but it **undermines statistical inference** (i.e., trusting the significance tests and confidence intervals).

---

<div align='center'>

## 🟦 A/B Testing, Causal Inference, and Difference-in-Differences (DID)

</div>

### A/B Testing

**Explanation:**  
**A/B Testing** (also known as split testing or randomized controlled experiments) is a statistical method used to compare two versions of a variable (A vs. B) to determine which one performs better. It is widely used in web development, marketing, product design, and business optimization.

**Key Elements:**
- Random assignment of users to Group A (control) or Group B (treatment)
- Clear success metric (e.g., click-through rate, conversion rate, revenue)
- Statistical significance testing (usually t-test or z-test)

**Example:**  
An e-commerce company wants to test two button colors:  
- Version A: Blue "Buy Now" button (control)  
- Version B: Green "Buy Now" button (treatment)  

After running the test on 10,000 users each:  
- Blue: 3.2% conversion rate  
- Green: 4.1% conversion rate  

If the difference is statistically significant, the company adopts the green button.

---

### Causal Inference

**Explanation:**  
**Causal Inference** is the process of drawing conclusions about **cause-and-effect** relationships from data, going beyond simple correlation. While correlation shows association, causal inference tries to answer “Does X *cause* Y?”

**Core Challenge:**  
Confounding variables, selection bias, and reverse causality make causal claims difficult from observational data.

**Common Methods:**  
- Randomized Controlled Trials (RCTs / A/B tests)
- Instrumental Variables (IV)
- Regression Discontinuity Design (RDD)
- Difference-in-Differences (DID)
- Propensity Score Matching

**Why it matters:**  
Business, policy, and scientific decisions require knowing what will *actually cause* an outcome, not just what is associated with it.

---

### Difference-in-Differences (DID)

**Explanation:**  
**Difference-in-Differences (DID)** is a statistical technique used in causal inference to estimate causal effects from observational (non-experimental) data. It compares the **change** in outcomes over time between a treatment group and a control group.

**Core Idea:**  
It subtracts the change in the control group from the change in the treatment group to isolate the treatment effect (assuming parallel trends).

**Formula:**
$$
DID = (Y_{Treatment, After} - Y_{Treatment, Before}) - (Y_{Control, After} - Y_{Control, Before})
$$

**Example: Minimum Wage Study**  
A state raises its minimum wage (Treatment). Researchers compare employment changes in that state vs. a neighboring state that did not raise wages (Control), before and after the policy.

- Treatment state employment change: -2%  
- Control state employment change: +1%  
- DID estimate: -3% (the policy caused a 3% drop in employment)

**Assumption:** Parallel Trends — In the absence of treatment, both groups would have followed similar trends.

**Applications:** Economics, public policy, healthcare, and social sciences.

---

<div align='center'>

## 🟦 ANCOVA and MANOVA

</div>

### ANCOVA (Analysis of Covariance)

**Explanation:**  
**ANCOVA** is a statistical technique that combines **ANOVA** and **regression**. It is used to compare the means of one or more groups while **controlling for the effect of one or more continuous covariates** (confounding variables).

**Purpose:**
- Increases statistical power by reducing error variance
- Adjusts group means to account for the covariate
- Tests whether group differences remain significant after adjusting for the covariate

**Key Assumptions:**
- Linearity between covariate and dependent variable
- Homogeneity of regression slopes (the relationship between covariate and DV is the same across groups)
- Homoscedasticity and normality of residuals

**Example:**  
A researcher wants to compare the effectiveness of three teaching methods (A, B, C) on student test scores, while controlling for students’ prior GPA (covariate).  

ANCOVA will tell whether there are significant differences between teaching methods **after adjusting for prior GPA**.

---

### MANOVA (Multivariate Analysis of Variance)

**Explanation:**  
**MANOVA** is an extension of ANOVA that allows the analysis of **multiple dependent variables** simultaneously. Instead of testing each dependent variable separately, MANOVA tests whether there are significant differences between groups across a combination of dependent variables.

**Purpose:**
- Controls the overall Type I error rate (avoids inflation from running multiple ANOVAs)
- Detects group differences that may not be visible when looking at variables individually
- Examines how groups differ on a linear combination of dependent variables

**Key Statistics:**
- Wilks’ Lambda, Pillai’s Trace, Hotelling’s Trace, Roy’s Largest Root

**Example:**  
A psychologist compares three types of therapy on patients using two outcome measures: Anxiety Score and Depression Score.

Instead of running two separate ANOVAs, MANOVA tests whether the therapies have a combined effect on both anxiety and depression together.

---

### Main Differences

| Aspect                  | ANOVA          | ANCOVA                     | MANOVA                     |
|-------------------------|----------------|----------------------------|----------------------------|
| Dependent Variables     | 1              | 1                          | 2 or more                  |
| Covariates              | None           | Yes (continuous)           | Optional                   |
| Main Purpose            | Compare groups | Compare groups + control   | Compare groups on multiple DVs |
| Complexity              | Low            | Medium                     | High                       |

These techniques are essential in experimental and quasi-experimental research for more accurate and powerful statistical analysis.

---

<div align='center'>

## 🟦 Monte Carlo Simulation

</div>

### Explanation
**Monte Carlo Simulation** is a powerful computational technique that uses repeated random sampling to obtain numerical results and solve complex problems. It is particularly useful when dealing with uncertainty, high-dimensional problems, or when analytical solutions are difficult or impossible to derive.

The name "Monte Carlo" comes from the Monte Carlo Casino in Monaco, reflecting the method’s reliance on randomness and probability — similar to games of chance.

### How It Works
1. Define a domain of possible inputs (probability distributions).
2. Randomly sample from these distributions many times (often thousands or millions of iterations).
3. Perform a deterministic computation for each sample.
4. Aggregate the results to obtain statistical estimates (mean, variance, probabilities, confidence intervals, etc.).

### Why We Use Monte Carlo Simulation
- Handles complex systems with many uncertain variables
- Provides approximate solutions to problems that are too difficult to solve analytically
- Quantifies risk and uncertainty
- Allows "what-if" scenario analysis

### Examples

**Example 1: Estimating π (Simple Monte Carlo)**
We can estimate the value of π by randomly throwing darts at a square that contains a quarter circle.

- Consider a unit square [0,1] × [0,1]
- Generate thousands of random points (x, y) where 0 ≤ x,y ≤ 1
- Count how many points fall inside the quarter circle ($x^2 + y^2 \leq 1$)
- Estimate: $\pi \approx 4 \times \frac{\text{points inside circle}}{\text{total points}}$

**Example 2: Investment Portfolio Risk**
An investor has a portfolio with three assets. Returns are uncertain and follow different probability distributions.

Using Monte Carlo:
- Simulate 10,000 possible future scenarios by randomly sampling returns for each asset
- Calculate the portfolio value for each scenario
- Analyze the distribution of outcomes:
  - Expected return
  - Probability of losing more than 10%
  - Value at Risk (VaR)

**Example 3: Project Management (PERT Analysis)**
Estimate project completion time when each task has uncertain duration (optimistic, most likely, pessimistic).

Monte Carlo simulates thousands of possible project timelines and produces a probability distribution of total project duration, helping managers understand the chance of finishing on time.

### Applications
- Finance (option pricing, risk analysis)
- Physics and Engineering
- Operations Research
- Statistics (Bayesian inference, bootstrap methods)
- Climate modeling and epidemiology

Monte Carlo Simulation is one of the most versatile tools in advanced statistics and data science for dealing with uncertainty.

---

<div align='center'>

## 🟦 Linear Programming

</div>

### Explanation
**Linear Programming (LP)** is a mathematical optimization technique used to find the best possible outcome (maximum or minimum) of a linear objective function, subject to a set of linear constraints. It is one of the most important tools in operations research, management science, and applied statistics.

The goal is to optimize (maximize or minimize) a linear function while satisfying a system of linear inequalities or equalities.

### Key Components
- **Decision Variables**: Variables you want to solve for (e.g., $x$, $y$).
- **Objective Function**: The linear function to be maximized or minimized.  
  Example: Maximize $Z = 3x + 5y$
- **Constraints**: Linear inequalities or equalities that limit the feasible region.  
  Example: $2x + y \leq 20$, $x + 3y \leq 30$, $x \geq 0$, $y \geq 0$
- **Feasible Region**: The set of all points that satisfy all constraints (usually a polygon in 2D).
- **Optimal Solution**: The point in the feasible region that gives the best value of the objective function.

### Methods to Solve Linear Programming Problems
- **Graphical Method** (for 2 variables)
- **Simplex Algorithm** (most common for larger problems)
- **Interior-Point Methods**
- Software tools: Excel Solver, Python (PuLP, SciPy), R, MATLAB

### Simple Example

**Problem:**  
A company produces two products: A and B.  
- Profit from A: $40 per unit  
- Profit from B: $30 per unit  

**Constraints:**  
- Production time: $2x + y \leq 100$ (hours)  
- Material: $x + 2y \leq 80$ (units)  
- $x \geq 0$, $y \geq 0$

**Objective:** Maximize profit $Z = 40x + 30y$

**Solution (Graphical/Inspection):**  
The optimal solution is usually found at one of the corner points of the feasible region.  

After solving, suppose the optimal point is $x = 40$, $y = 20$.  
Then maximum profit $Z = 40(40) + 30(20) = 1600 + 600 = 2200$.

### Applications
- Resource allocation and production planning
- Portfolio optimization in finance
- Diet and nutrition planning
- Transportation and logistics (shipping costs)
- Blending problems (oil refining, animal feed)
- Scheduling and workforce allocation

Linear Programming is extremely powerful when relationships are linear. When relationships become non-linear, more advanced techniques like Integer Programming, Quadratic Programming, or Nonlinear Programming are used.