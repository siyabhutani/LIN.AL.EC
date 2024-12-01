#7C
def compute_det(matrix):
    def swap_rows(mat, i, j):
        mat[i], mat[j] = mat[j], mat[i]

    def scale_row(mat, i, factor):
        mat[i] = [elem * factor for elem in mat[i]]

    def add_multiple_of_row(mat, source, target, multiple):
        mat[target] = [x + y * multiple for x, y in zip(mat[target], mat[source])]

    size = len(matrix)
    mat_copy = [row[:] for row in matrix]
    scale_factor = 1
    transpositions = 0

    for col in range(size):
        pivot = col
        while pivot < size and mat_copy[pivot][col] == 0:
            pivot += 1

        if pivot == size:
            return 0

        if pivot != col:
            swap_rows(mat_copy, pivot, col)
            transpositions += 1

        scale_value = mat_copy[col][col]
        scale_row(mat_copy, col, 1 / scale_value)
        scale_factor *= scale_value

        for row in range(size):
            if row != col:
                add_multiple_of_row(mat_copy, col, row, -mat_copy[row][col])

    product_diag = 1
    for i in range(size):
        product_diag *= mat_copy[i][i]

    determinant = product_diag * scale_factor * ((-1) ** transpositions)
    return determinant

# Example usage
matrix = [
    [2, 1, 1],
    [4, -6, 0],
    [-2, 7, 2]
]
result = compute_det(matrix)
print("Determinant:", result)
