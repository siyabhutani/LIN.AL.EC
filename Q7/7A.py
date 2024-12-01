#7A
def determinant(matrix):
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    total = 0
    for index in range(size):
        minor = []
        for row in range(1, size):
            temp = []
            for col in range(size):
                if col != index:
                    temp.append(matrix[row][col])
            minor.append(temp)
        sign = (-1) ** index
        total += sign * matrix[0][index] * determinant(minor)
    return total

# Example Usage
matrix = [
    [3, 2, 1],
    [4, 5, 6],
    [7, 8, 9]
]
result = determinant(matrix)
print(result)
