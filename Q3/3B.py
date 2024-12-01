#3B
def reduced_row_echelon_form(matrix, display_operations=False):
    def swap_rows(mat, row1, row2):
        mat[row1], mat[row2] = mat[row2], mat[row1]
        return mat

    def scale_row(mat, row, factor):
        mat[row] = [elem * factor for elem in mat[row]]
        return mat

    def add_scaled_row(mat, source_row, target_row, factor):
        mat[target_row] = [mat[target_row][i] + factor * mat[source_row][i] for i in range(len(mat[0]))]
        return mat

    rows = len(matrix)
    cols = len(matrix[0])
    mat_copy = [row[:] for row in matrix]
    operations_log = []
    elementary_matrices = []

    pivot_row = 0

    for col in range(cols):
        if pivot_row >= rows:
            break

        if mat_copy[pivot_row][col] == 0:
            for r in range(pivot_row + 1, rows):
                if mat_copy[r][col] != 0:
                    mat_copy = swap_rows(mat_copy, pivot_row, r)
                    if display_operations:
                        operations_log.append(f"Swapped row {pivot_row + 1} with row {r + 1}")
                        elementary_matrices.append(generate_swap_matrix(rows, pivot_row, r))
                    break

        if mat_copy[pivot_row][col] != 0:
            pivot = mat_copy[pivot_row][col]
            mat_copy = scale_row(mat_copy, pivot_row, 1 / pivot)
            if display_operations:
                operations_log.append(f"Scaled row {pivot_row + 1} by {1 / pivot}")
                elementary_matrices.append(generate_scale_matrix(rows, pivot_row, 1 / pivot))

            for r in range(rows):
                if r != pivot_row and mat_copy[r][col] != 0:
                    factor = -mat_copy[r][col]
                    mat_copy = add_scaled_row(mat_copy, pivot_row, r, factor)
                    if display_operations:
                        operations_log.append(f"Added {factor} * row {pivot_row + 1} to row {r + 1}")
                        elementary_matrices.append(generate_add_matrix(rows, pivot_row, r, factor))
            pivot_row += 1

    if display_operations:
        print("Row Operations:")
        for op in operations_log:
            print(op)
        print("\nElementary Matrices:")
        for mat in elementary_matrices:
            print(mat)

    return mat_copy

def generate_swap_matrix(size, r1, r2):
    E = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    E[r1], E[r2] = E[r2], E[r1]
    return E

def generate_scale_matrix(size, row, scalar):
    E = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    E[row][row] = scalar
    return E

def generate_add_matrix(size, source_row, target_row, scalar):
    E = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
    E[target_row][source_row] = scalar
    return E

matrix_example = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

rref_matrix = reduced_row_echelon_form(matrix_example)
print("RREF:")
for row in rref_matrix:
    print(row)

rref_matrix_with_operations = reduced_row_echelon_form(matrix_example, display_operations=True)
print("\nRREF with row operations and elementary matrices:")
for row in rref_matrix_with_operations:
    print(row)
