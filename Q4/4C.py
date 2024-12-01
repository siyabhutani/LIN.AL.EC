#4C
def solve_linear_equations(matrix, results):
    def gauss_elimination(mat, res):
        size = len(res)
        for row in range(size):
            max_row = row
            for search in range(row + 1, size):
                if abs(mat[search][row]) > abs(mat[max_row][row]):
                    max_row = search
            mat[row], mat[max_row] = mat[max_row], mat[row]
            res[row], res[max_row] = res[max_row], res[row]
            
            pivot = mat[row][row]
            for col in range(row, size):
                mat[row][col] = mat[row][col] / pivot
            res[row] = res[row] / pivot
            
            for down in range(row + 1, size):
                factor = mat[down][row]
                for col in range(row, size):
                    mat[down][col] -= factor * mat[row][col]
                res[down] -= factor * res[row]
        
        solution = [0] * size
        for row in range(size - 1, -1, -1):
            total = sum(mat[row][j] * solution[j] for j in range(row + 1, size))
            solution[row] = res[row] - total
        return solution

    def is_consistent(A):
        return all(any(abs(value) > 1e-10 for value in row) for row in A)

    if is_consistent(matrix):
        return gauss_elimination(matrix, results)
    else:
        return "System is inconsistent"

# Example usage:
A = [
    [2, -1, 1],
    [1, 1, -1],
    [1, -1, 2]
]
b = [6, 3, 14]

solution = solve_linear_equations(A, b)
print(solution)
