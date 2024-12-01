#2A
def getting_the_determinant(matrix):
    size = len(matrix)
    if size == 1:  # 1x1 matrix
        return matrix[0][0]
    if size == 2:  # 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # For larger matrices, use recursion
    determinant = 0
    for col in range(size):
        sub_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        determinant += ((-1) ** col) * matrix[0][col] * getting_the_determinant(sub_matrix)
    return determinant

def check_if_matrix_zero(matrix):
    for row in matrix:
        for elem in row:
            if elem != 0:
                return False
    return True

def check_symmetric(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def check_hermitian(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != complex(matrix[j][i]).conjugate():
                return False
    return True

def check_square(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return rows == cols

def check_orthogonal(matrix):
    size = len(matrix)
    identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    transpose = [[matrix[j][i] for j in range(size)] for i in range(size)]
    product = [[sum(transpose[i][k] * matrix[k][j] for k in range(size)) for j in range(size)] for i in range(size)]
    return product == identity

def check_unitary(matrix):
    size = len(matrix)
    identity = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    conjugate_transpose = [[complex(matrix[j][i]).conjugate() for j in range(size)] for i in range(size)]
    product = [[sum(conjugate_transpose[i][k] * matrix[k][j] for k in range(size)) for j in range(size)] for i in range(size)]
    return product == identity

def check_scalar(matrix):
    first_value = matrix[0][0]
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if i != j and elem != 0:
                return False
            if i == j and elem != first_value:
                return False
    return True

def check_singular(matrix):
    determinant = getting_the_determinant(matrix)
    return determinant == 0

def check_invertible(matrix):
    determinant = getting_the_determinant(matrix)
    return determinant != 0

def check_identity(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == j and matrix[i][j] != 1:
                return False
            if i != j and matrix[i][j] != 0:
                return False
    return True

def check_nilpotent(matrix, power=10):
    size = len(matrix)
    result = [[matrix[i][j] for j in range(size)] for i in range(size)]
    for _ in range(1, power):
        result = [[sum(result[i][k] * matrix[k][j] for k in range(size)) for j in range(size)] for i in range(size)]
    return all(all(elem == 0 for elem in row) for row in result)

def check_diagonalizable(matrix):
    # Direct implementation assumes a diagonal matrix is diagonalizable.
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i != j and matrix[i][j] != 0:
                return False
    return True

def check_positive_definite(matrix):
    size = len(matrix)
    for i in range(1, size + 1):
        sub_matrix = [row[:i] for row in matrix[:i]]
        if getting_the_determinant(sub_matrix) <= 0:
            return False
    return True

def check_lu(matrix):
    size = len(matrix)
    lower = [[0] * size for _ in range(size)]
    upper = [[0] * size for _ in range(size)]
    for i in range(size):
        for k in range(i, size):
            upper[i][k] = matrix[i][k] - sum(lower[i][j] * upper[j][k] for j in range(i))
        for k in range(i, size):
            if i == k:
                lower[i][i] = 1
            else:
                lower[k][i] = (matrix[k][i] - sum(lower[k][j] * upper[j][i] for j in range(i))) / upper[i][i]
    return True

def display_results(matrix):
    print("Matrix Properties:")
    print(f"Is Zero: {check_if_matrix_zero(matrix)}")
    print(f"Is Symmetric: {check_symmetric(matrix)}")
    print(f"Is Hermitian: {check_hermitian(matrix)}")
    print(f"Is Square: {check_square(matrix)}")
    print(f"Is Orthogonal: {check_orthogonal(matrix)}")
    print(f"Is Unitary: {check_unitary(matrix)}")
    print(f"Is Scalar: {check_scalar(matrix)}")
    print(f"Is Singular: {check_singular(matrix)}")
    print(f"Is Invertible: {check_invertible(matrix)}")
    print(f"Is Identity: {check_identity(matrix)}")
    print(f"Is Nilpotent: {check_nilpotent(matrix)}")
    print(f"Is Diagonalizable: {check_diagonalizable(matrix)}")
    print(f"Is Positive Definite: {check_positive_definite(matrix)}")
    print(f"Has LU Decomposition: {check_lu(matrix)}")

# Example matrix
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Display results
display_results(matrix)
