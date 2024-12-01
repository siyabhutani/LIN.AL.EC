#3E
def matrix_rank_decomposition(input_matrix):
    def extract_independent_rows(matrix):
        m, n = len(matrix), len(matrix[0])
        row_indices = []
        pivot_cols = []
        temp_matrix = [row[:] for row in matrix]
        for i in range(min(m, n)):
            pivot_found = False
            for r in range(i, m):
                if temp_matrix[r][i] != 0:
                    pivot_found = True
                    temp_matrix[r], temp_matrix[i] = temp_matrix[i], temp_matrix[r]
                    break
            if pivot_found:
                row_indices.append(i)
                pivot_cols.append(i)
                for j in range(i + 1, m):
                    factor = temp_matrix[j][i] / temp_matrix[i][i]
                    for k in range(n):
                        temp_matrix[j][k] -= factor * temp_matrix[i][k]
        return row_indices, pivot_cols

    def build_matrix_from_indices(original, indices, axis):
        return [[original[i][j] if axis == 0 else original[j][i] for j in indices] for i in range(len(original)) if axis == 0 or i in indices]

    independent_rows, pivot_columns = extract_independent_rows(input_matrix)
    matrix_r = build_matrix_from_indices(input_matrix, pivot_columns, 1)
    matrix_b = build_matrix_from_indices(input_matrix, independent_rows, 0)
    return matrix_r, matrix_b


original_matrix = [[4, 2, 3], [6, 3, 9], [2, 1, 2]]
R, B = matrix_rank_decomposition(original_matrix)
print("R (independent columns):", R)
print("B (independent rows):", B)
