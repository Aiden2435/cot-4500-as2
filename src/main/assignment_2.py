import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)

#Question 1
def nevilles_method(x_points, y_points,x):
    x_points=[3.6,3.8,3.9]
    y_points=[1.675,1.436,1.318]
    matrix = np.zeros((3,3))

    for counter, row in enumerate(matrix):
        row[0] = y_points[counter]
    num_of_points = len(x_points)
    for i in range(1, num_of_points):
        for j in range(1, i+1):
            multi1 = (x - x_points[i-j]) * matrix[i][j-1]
            multi2 = (x - x_points[i]) * matrix[i-1][j-1]
            denominator = x_points[i] - x_points[i-j]

            coefficient = (multi1-multi2)/denominator
            matrix[i][j] = coefficient
    
    print(matrix[num_of_points-1][num_of_points-1])
if __name__ == "__main__":

    x_points = []
    y_points = []
#Question 2
    approximating_value = 3.7
    nevilles_method(x_points, y_points, approximating_value)
#Question 3
def divided_difference_table(x_points, y_points):
    size: int = len(x_points)
    matrix: np.array = np.zeros((size, size), dtype=object)
    
    for index, row in enumerate(matrix):
        row[0] = (y_points[index])
    

    for i in range(1, size):
        for j in range(1, i+1):
            numerator = matrix[i][j-1] - matrix[i-1][j-1]
            denominator = (x_points[i]) - (x_points[i-j])
            operation = numerator / denominator
          
            matrix[i][j] = operation
    list=[matrix[1][1],matrix[2][2],matrix[3][3]]
    print(list)        
    return matrix
   
def get_approximate_result(matrix, x_points, value):
    reoccuring_x_span = 1
    reoccuring_px_result = matrix[0][0]
    
    for index in range(1, len(matrix)):
        polynomial_coefficient = matrix[index][index]
        reoccuring_x_span *= ((value - x_points[index-1]))
        
        mult_operation = polynomial_coefficient * reoccuring_x_span
        reoccuring_px_result += mult_operation
    return reoccuring_px_result
if __name__ == "__main__":
    x_points = [7.2, 7.4, 7.5, 7.6]
    y_points = [23.5492, 25.3913, 26.8224, 27.4589]
    divided_table = divided_difference_table(x_points, y_points)
    approximating_x = 7.3
    final_approximation = get_approximate_result(divided_table, x_points, approximating_x)
    print("%.15f" % final_approximation, "\n")


#Question 4
def apply_div_dif(matrix: np.array):
    size = len(matrix)
    for i in range(2, size):
        for j in range(2, i+2):
           
            if j >= len(matrix[i]) or matrix[i][j] != 0:
                continue
            
            left: float =  matrix[i][j-1]
            diagonal_left: float = matrix[i-1][j-1]
            numerator: float = left - diagonal_left
            denominator = matrix[i][0] - matrix[i-(j-1)][0]
            operation = numerator / denominator
            matrix[i][j] = operation
    
    return matrix
if __name__ == "__main__":    
    x_points = [3.6, 3.8, 3.9]
    y_points = [1.675, 1.436, 1.318]
    slopes = [-1.195, -1.188, -1.182]
    num_of_points = len(x_points)
    matrix = np.zeros((2*num_of_points, 2*num_of_points))
    for x in range(num_of_points):
        matrix[2*x][0] = x_points[x]
        matrix[2*x+1][0] = x_points[x]
    
    for x in range(num_of_points):
        matrix[2*x][1] = y_points[x]
        matrix[2*x+1][1] = y_points[x]
    for x in range(num_of_points):
        matrix[2*x+1][2] = slopes[x]
    filled_matrix = apply_div_dif(matrix)
    print(filled_matrix)
    
#Question 5
x = np.array([2, 5, 8, 10])
y  = np.array([3, 5, 7, 9])
n = len(x)-1
A = np.zeros((n+1, n+1))
A[0, 0] = 1
A[n, n] = 1
for i in range(1, n):
    A[i, i-1] = x[i] -x[i-1]
    A[i, i] = 2 * (x[i+1] - x[i-1])
    A[i, i+1] = x[i+1] - x[i]
b = np.zeros(n+1)
for i in range(1, n):
    b[i] = 3 * (y[i+1] - y[i]) / (x[i+1] - x[i]) - \
           3 * (y[i] - y[i-1]) / (x[i] - x[i-1])
x = np.linalg.solve(A, b)
print(A, "\n")
print(b, "\n")
print(x, "\n")
