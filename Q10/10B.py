#10B
def decompose_matrix(matrix):
    n = len(matrix)
    lower_triangular = [[0.0] * n for _ in range(n)]
    
    for row in range(n):
        for col in range(row + 1):
            sum_elements = 0.0
            for k in range(col):
                sum_elements += lower_triangular[row][k] * lower_triangular[col][k]
            
            if row == col:
                lower_triangular[row][col] = (matrix[row][row] - sum_elements) ** 0.5
            else:
                lower_triangular[row][col] = (matrix[row][col] - sum_elements) / lower_triangular[col][col]
    
    return lower_triangular

# Example usage:
matrix_input = [
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]
]

result = decompose_matrix(matrix_input)

for row in result:
    print(row)
