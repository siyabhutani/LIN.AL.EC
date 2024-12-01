#4A
class EquationSolver:
    def __init__(self, mat, vec):
        if len(mat) != len(vec) or any(len(row) != len(mat) for row in mat):
            raise ValueError("Matrix and vector dimensions are incompatible.")
        self.matrix = mat
        self.vector = vec

    def gaussian_elim(self):
        size = len(self.matrix)
        for pivot in range(size):
            max_row = pivot
            for row in range(pivot + 1, size):
                if abs(self.matrix[row][pivot]) > abs(self.matrix[max_row][pivot]):
                    max_row = row
            self.matrix[pivot], self.matrix[max_row] = self.matrix[max_row], self.matrix[pivot]
            self.vector[pivot], self.vector[max_row] = self.vector[max_row], self.vector[pivot]
            for row in range(pivot + 1, size):
                factor = self.matrix[row][pivot] / self.matrix[pivot][pivot]
                for col in range(pivot, size):
                    self.matrix[row][col] -= factor * self.matrix[pivot][col]
                self.vector[row] -= factor * self.vector[pivot]

    def back_substitute(self):
        size = len(self.vector)
        result = [0] * size
        for i in range(size - 1, -1, -1):
            temp_sum = self.vector[i]
            for j in range(i + 1, size):
                temp_sum -= self.matrix[i][j] * result[j]
            result[i] = temp_sum / self.matrix[i][i]
        return result

    def solve(self):
        self.gaussian_elim()
        return self.back_substitute()

# Example:
matrix = [[2, -1, 1], [1, 3, 2], [1, -1, 2]]
vector = [8, 13, 5]
system = EquationSolver(matrix, vector)
solution = system.solve()
print(solution)
