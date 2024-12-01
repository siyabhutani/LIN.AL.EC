#3C
def check_linear_independence(vectors):
    n = len(vectors)
    m = len(vectors[0])
    matrix = [vec[:] for vec in vectors]
    
    def reduce_matrix(mat):
        rows = len(mat)
        cols = len(mat[0])
        for lead in range(min(rows, cols)):
            row = lead
            while row < rows and mat[row][lead] == 0:
                row += 1
            if row == rows:
                continue
            mat[row], mat[lead] = mat[lead], mat[row]
            divisor = mat[lead][lead]
            for col in range(cols):
                mat[lead][col] /= divisor
            for r in range(rows):
                if r != lead:
                    multiplier = mat[r][lead]
                    for c in range(cols):
                        mat[r][c] -= multiplier * mat[lead][c]
        return mat

    result_matrix = reduce_matrix(matrix)
    zero_rows = sum(all(val == 0 for val in row) for row in result_matrix)
    return "Independent" if zero_rows == 0 else "Dependent"

# Example input
vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(check_linear_independence(vectors))
