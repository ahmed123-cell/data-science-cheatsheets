import numpy as np
import matplotlib.pyplot as plt
from pulp import LpProblem, LpVariable, LpStatus, LpMaximize, LpMinimize, PULP_CBC_CMD, value


""" linear programming optimization problem """
prob = LpProblem("Maximize_profit", LpMaximize)  # Create the problem

# Create variables
A = LpVariable("Units_of_A", lowBound=0, cat='Integer')
B = LpVariable("Units_of_B", lowBound=0, cat='Integer')

# Objective function
prob += 20 * A + 30 * B, "Total_Profit"

# Create constraints
prob += 2 * A + 5 * B <= 120, 'Labor_Hours'
prob += 4 * A + 3 * B <= 120, "Raw_Material"

prob.solve(PULP_CBC_CMD(msg=False)) # solve the problem and print to much detail

# print the results
print("Status: ", LpStatus[prob.status])
print(f"The number of units of A: {A.varValue}")
print(f"The number of units of B: {B.varValue}")
print(f"The maximum profit: {value(prob.objective)} dollars")
#---------------------------------------------------------------------------------------------------
# Monte Carlo Simualtion problem
np.random.seed(42)

n_simulations = 10000 # number of simulations

# define the expected costs with the standard deviation(proportion)
costs = {
    'building materials': (100000, 0.20),
    'employee': (80000, 0.15),
    'tools': (50000, 0.25),
    'extra costs': (20000, 0.30)
}
total_costs = [] # calculate the total cost for each simulation

for _ in range(n_simulations):
    simulation_cost = 0
    for mean, std_ratio in costs.values():

        cost = np.random.normal(mean, std_ratio*mean)

        cost = max(cost, 0)
        simulation_cost += cost
    total_costs.append(simulation_cost)

total_costs = np.array(total_costs) # convert the list to array 

# Calculate important statistics
mean_cost = np.mean(total_costs)
median_cost = np.median(total_costs)
percentile_5 = np.percentile(total_costs, 5)
percentile_95 = np.percentile(total_costs, 95)
prob_over_270k = np.sum(total_costs > 270000) / n_simulations * 100

# Print the results
print(f"The mean expected cost: {mean_cost:,.0f} dollars")
print(f"The median: {median_cost:,.0f} dollars")
print(f"(The best scenatio) proportion 5%: {percentile_5:,.0f} dollars")
print(f"(The worst scenario) proportion 95%: {percentile_95:,.0f} dollars")
print(f"The probability of costs exceeds 270,000 dollars: {prob_over_270k:.1f}%")

# plot a histogram to distribure the costs
plt.figure(figsize=(10, 6))
plt.hist(total_costs, bins=50, color='skyblue', alpha=0.7, edgecolor='black')
plt.axvline(mean_cost, color='red', linestyle='--', label=f'mean: {mean_cost:,.0f}')
plt.axvline(percentile_95, color='orange', linestyle='--', label=f'95% percentile: {percentile_95:,.0f}')
plt.title("the distribution of the total costs for the project (monte carlo simulation 10,000 times)".title())
plt.xlabel("The total costs ($)")
plt.ylabel("The number of times")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()