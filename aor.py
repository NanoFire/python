import numpy as np
from scipy.optimize import linprog


"""
scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None,
method='highs', callback=None, options=None, x0=None, integrality=None)
"""

# Coefficients for the objective function (c) (-c for maximization problem)
c = np.array([2, 3, 1])

# Coefficients matrix for the constraints (A)
A = np.array([[1, 2, 2],
              [3, 2, 0],
              [1, 1, 3]])

# Right-hand side vector for the constraints (b)
b = np.array([8, 5, 6])

# Bounds for decision variables (x >= 0)
x_bounds = [(0, None), (0, None), (0, None)]



# Solve the linear programming problem
result = linprog(-c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs') # -c for max

#integer programming
#result = linprog(-c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs',integrality=[1,1,1])

# Extract the solution
x_solution = result.x
maximized_value = result.fun

print("Optimal Solution:")
print(f"x = {x_solution}")
print(f"maximized Value = {-maximized_value}")