#4F
class LinearEquationSolver:
    def __init__(self, coefficients, constants):
        self.coefficients = coefficients
        self.constants = constants

        if len(coefficients) != len(constants):
            raise ValueError("Mismatch: The number of rows in the matrix must equal the size of the constants vector.")
        for row in coefficients:
            if len(row) != len(coefficients[0]):
                raise ValueError("Invalid matrix: All rows must have the same number of columns.")

    def solve_system(self):
        perm_matrix, lower, upper = self.perform_plu(self.coefficients)
        if perm_matrix is None or lower is None or upper is None:
            return "Error: PLU decomposition could not be completed."

        permuted_constants = self.apply_permutation(self.constants, perm_matrix)
        intermediate = self.forward_solve(lower, permuted_constants)
        solution = self.backward_solve(upper, intermediate)

        return solution

    def perform_plu(self, matrix):
        n = len(matrix)
        perm_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        lower_tri = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
        upper_tri = [row[:] for row in matrix]

        for col in range(n):
            pivot_row = col
            for row in range(col + 1, n):
                if abs(upper_tri[row][col]) > abs(upper_tri[pivot_row][col]):
                    pivot_row = row
            if upper_tri[pivot_row][col] == 0:
                return None, None, None
            if pivot_row != col:
                upper_tri[col], upper_tri[pivot_row] = upper_tri[pivot_row], upper_tri[col]
                perm_matrix[col], perm_matrix[pivot_row] = perm_matrix[pivot_row], perm_matrix[col]
            for row in range(col + 1, n):
                factor = upper_tri[row][col] / upper_tri[col][col]
                lower_tri[row][col] = factor
                for k in range(n):
                    upper_tri[row][k] -= factor * upper_tri[col][k]
        return perm_matrix, lower_tri, upper_tri

    def apply_permutation(self, vec, perm):
        return [sum(perm[i][j] * vec[j] for j in range(len(vec))) for i in range(len(perm))]

    def forward_solve(self, lower, constants):
        n = len(lower)
        y = [0] * n
        for i in range(n):
            y[i] = constants[i] - sum(lower[i][j] * y[j] for j in range(i))
        return y

    def backward_solve(self, upper, intermediate):
        n = len(upper)
        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = (intermediate[i] - sum(upper[i][j] * x[j] for j in range(i + 1, n))) / upper[i][i]
        return x


# Example usage
example_matrix = [
    [2, 1, 1],
    [1, 3, 2],
    [1, 2, 3]
]
example_vector = [7, 10, 13]

try:
    solver = LinearEquationSolver(example_matrix, example_vector)
    result = solver.solve_system()
    print("Solution to the system:", result)
except ValueError as error:
    print(error)
