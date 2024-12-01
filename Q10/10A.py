#10A
def polar_decomposition(matrix):
    def transpose(mat):
        rows, cols = len(mat), len(mat[0])
        return [[mat[j][i] for j in range(rows)] for i in range(cols)]

    def matrix_multiply(mat1, mat2):
        return [[sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2))) for j in range(len(mat2[0]))] for i in range(len(mat1))]

    def identity_matrix(size):
        return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    def invert_matrix(mat):
        size = len(mat)
        augmented = [row + id_row for row, id_row in zip(mat, identity_matrix(size))]
        for i in range(size):
            pivot = augmented[i][i]
            for j in range(2 * size):
                augmented[i][j] /= pivot
            for k in range(size):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2 * size):
                        augmented[k][j] -= factor * augmented[i][j]
        return [row[size:] for row in augmented]

    def sqrt_matrix(mat):
        size = len(mat)
        approx = identity_matrix(size)
        for _ in range(20):  # Iterative refinement
            inv_approx = invert_matrix(approx)
            approx = [[(approx[i][j] + inv_approx[i][j]) / 2 for j in range(size)] for i in range(size)]
        return approx

    t_matrix = transpose(matrix)
    gram = matrix_multiply(t_matrix, matrix)
    root_gram = sqrt_matrix(gram)
    u_part = invert_matrix(root_gram)
    u = matrix_multiply(matrix, u_part)
    return u, root_gram


# Example usage:
A = [[4, 0], [3, -5]]  # Example input matrix
U, P = polar_decomposition(A)

print("U (Unitary Matrix):")
for row in U:
    print(row)

print("\nP (Positive Semi-Definite Matrix):")
for row in P:
    print(row)
