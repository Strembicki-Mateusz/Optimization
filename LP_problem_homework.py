import numpy as np
from scipy.optimize import minimize

def production(x):
    x1, x2, x3 = x
    return - (1.5 * x1**0.85 * x2**0.6 * x3**0.75)  # Negative for maximization

def cost_constraint(x):
    x1, x2, x3 = x
    return 10000 - (7*x1 + 3*x2 + 5*x3 + 30)

# Initial guess
x0 = [100, 100, 100]

# Bounds for x1, x2, x3 (must be non-negative)
bounds = [(0, None), (0, None), (0, None)]

# Constraint dictionary
constraints = ({'type': 'ineq', 'fun': cost_constraint})

# Solve the optimization problem
solution = minimize(production, x0, bounds=bounds, constraints=constraints, method='SLSQP')

# Results
optimal_x1, optimal_x2, optimal_x3 = solution.x
y_optimal = -solution.fun  # Convert back to positive

print(f"Optimal x1: {optimal_x1:.2f}")
print(f"Optimal x2: {optimal_x2:.2f}")
print(f"Optimal x3: {optimal_x3:.2f}")
print(f"Maximum production y: {y_optimal:.2f}")
