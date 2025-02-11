def neville(x_values, f_values, x):
    n = len(x_values)
    # Create a table for storing intermediate results
    P = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize the diagonal with f(x_i) values
    for i in range(n):
        P[i][i] = f_values[i]

    # Apply Neville's formula to calculate the interpolation values
    for j in range(1, n):
        for i in range(n - j):
            P[i][i + j] = ((x - x_values[i]) * P[i + 1][i + j] - (x - x_values[i + j]) * P[i][i + j - 1]) / (x_values[i + j] - x_values[i])

    # The final result is stored in P[0][n-1]
    return P[0][n - 1]

# Given data points
x_values = [3.6, 3.8, 3.9]
f_values = [1.675, 1.436, 1.318]

# Desired x value
x = 3.7

# Find the interpolated value using Neville's method
result = neville(x_values, f_values, x)

# Print the result
print(f"f({x}) = {result}")


import math

# Given data
x_values = [7.2, 7.4, 7.5, 7.6]
f_values = [23.5492, 25.3913, 26.8224, 27.4589]

# Function to compute the forward divided differences table
def compute_divided_differences(x_vals, f_vals):
    n = len(x_vals)
    table = [[0] * n for _ in range(n)]
    
    # Initialize the first column with f(x) values
    for i in range(n):
        table[i][0] = f_vals[i]
    
    # Fill in the divided difference table
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_vals[i + j] - x_vals[i])
    
    return table

# Function to calculate the Newton's Forward Polynomial approximation
def newtons_forward_polynomial(x, x_vals, table, degree):
    n = len(x_vals)
    result = table[0][0]
    term = 1  # Initialize the first term as 1 (x - x0)^0
    
    for j in range(1, degree + 1):
        term *= (x - x_vals[j - 1])  # (x - x0)(x - x1)(x - x2)...
        result += term * table[0][j]
    
    return result

# Compute divided differences table
table = compute_divided_differences(x_values, f_values)

# Print the divided difference table
print("Divided Difference Table:")
for row in table:
    print(row)

# Degrees for approximations
degrees = [1, 2, 3]

# Calculate and print the polynomial approximations for degrees 1, 2, and 3 at a sample x = 7.5
x_sample = 7.5

for degree in degrees:
    approx_value = newtons_forward_polynomial(x_sample, x_values, table, degree)
    print(f"\nNewton's Forward Polynomial approximation for degree {degree} at x = {x_sample}: {approx_value}")

