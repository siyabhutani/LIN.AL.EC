#4B
def is_consistent_system(matrix, values):
    def forward_elimination(mat, vec):
        for pivot in range(len(mat)):
            max_row = pivot
            for row in range(pivot + 1, len(mat)):
                if abs(mat[row][pivot]) > abs(mat[max_row][pivot]):
                    max_row = row

            mat[pivot], mat[max_row] = mat[max_row], mat[pivot]
            vec[pivot], vec[max_row] = vec[max_row], vec[pivot]

            for row in range(pivot + 1, len(mat)):
                multiplier = mat[row][pivot] / mat[pivot][pivot]
                for col in range(pivot, len(mat[0])):
                    mat[row][col] -= multiplier * mat[pivot][col]
                vec[row] -= multiplier * vec[pivot]

    def check_consistency(mat, vec):
        for i in range(len(mat) - 1, -1, -1):
            if all(mat[i][j] == 0 for j in range(len(mat[0]))) and vec[i] != 0:
                return False
        return True

    augmented_matrix = [matrix[i] + [values[i]] for i in range(len(matrix))]
    coefficients = [row[:-1] for row in augmented_matrix]
    constants = [row[-1] for row in augmented_matrix]

    forward_elimination(coefficients, constants)
    return check_consistency(coefficients, constants)


# Example usage:
coefficients_matrix = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
constants_vector = [8, -11, -3]

result = is_consistent_system(coefficients_matrix, constants_vector)
print("Consistent" if result else "Inconsistent")
