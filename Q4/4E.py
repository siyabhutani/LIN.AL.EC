#4E
def matrix_to_rref(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    r = 0

    for c in range(cols):
        if r >= rows:
            break
        pivot = r
        for i in range(r, rows):
            if abs(matrix[i][c]) > abs(matrix[pivot][c]):
                pivot = i
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]

        if matrix[r][c] == 0:
            continue

        pivot_value = matrix[r][c]
        for j in range(c, cols):
            matrix[r][j] /= pivot_value

        for i in range(rows):
            if i != r:
                factor = matrix[i][c]
                for j in range(c, cols):
                    matrix[i][j] -= factor * matrix[r][j]
        r += 1

def express_solution(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) - 1
    solution = []

    for i in range(rows):
        if matrix[i][i] == 1:
            var = f"x{i} = {matrix[i][-1]}"
            for j in range(i + 1, cols):
                if matrix[i][j] != 0:
                    var += f" - ({matrix[i][j]} * x{j})"
            solution.append(var)
        elif all(matrix[i][j] == 0 for j in range(cols)) and matrix[i][-1] != 0:
            return "No solution"
    return solution if solution else "Infinite solutions"

def solution_set(augmented_matrix):
    matrix_to_rref(augmented_matrix)
    return express_solution(augmented_matrix)

# Example input
augmented = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

result = solution_set(augmented)
print(result)
