import numpy as np
from scipy import stats

# ===================== Confindence Interval ===================== # 

data = [12, 15, 14, 10, 13, 16, 18, 14]

n = len(data)
mean = np.mean(data)
std = np.std(data, ddof=1)

confidence = 0.95
alpha = 1 - confidence

t_value = stats.t.ppf(1 - alpha/2, df=n-1)

margin_error = t_value * (std / np.sqrt(n))

ci = (mean - margin_error, mean + margin_error)

print("CI:", ci)

# ========================= One Sample t-test ========================= # 

data = [12, 15, 14, 10, 13, 16]
population_mean = 14

t_stat, p_value = stats.ttest_1samp(data, population_mean)

print(t_stat, p_value)

alpha = 0.05
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# ========================= Two Sample t-test ========================= #

group1 = [12, 15, 14, 10]
group2 = [18, 17, 16, 19]

t_stat, p_value = stats.ttest_ind(group1, group2)

print(t_stat, p_value)

alpha = 0.05
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# ========================= Paired t-test ========================= #
before = [20, 21, 19, 22]
after = [23, 24, 22, 25]

t_stat, p_value = stats.ttest_rel(before, after)

print(t_stat, p_value)

alpha = 0.05
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")

# ========================= Chi-Square test ======================= # 
from scipy.stats import chi2_contingency

data = np.array([
    [30, 20],
    [10, 40]
])

chi2, p, df, expected = chi2_contingency(data)

print("Chi2:", chi2)
print("p-value:", p)
print("df:", df)
print("Expected:\n", expected)

if p < 0.05:
    print("Reject H0 → variables are dependent")
else:
    print("Fail to reject H0 → independent")

# ========================= ANOVA ======================= # 
from scipy.stats import f_oneway

group_a = [70, 72, 68, 71]
group_b = [75, 78, 74, 76]
group_c = [80, 82, 79, 81]

f_stat, p_value = f_oneway(group_a, group_b, group_c)

print("F-statistic:", f_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Reject H0 → at least one group differs")
else:
    print("Fail to reject H0")