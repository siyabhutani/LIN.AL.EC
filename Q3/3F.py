#3F
def lu_decomposition(matrix):
    size = len(matrix)
    lower = [[0] * size for _ in range(size)]
    upper = [[0] * size for _ in range(size)]

    for r in range(size):
        for c in range(r, size):
            total = 0
            for k in range(r):
                total += lower[r][k] * upper[k][c]
            upper[r][c] = matrix[r][c] - total

        for c in range(r, size):
            if r == c:
                lower[r][r] = 1
            else:
                total = 0
                for k in range(r):
                    total += lower[c][k] * upper[k][r]
                if upper[r][r] == 0:
                    raise ValueError("LU decomposition not possible (singular matrix).")
                lower[c][r] = (matrix[c][r] - total) / upper[r][r]
    
    return lower, upper

def invoke_lu(input_matrix):
    try:
        l_matrix, u_matrix = lu_decomposition(input_matrix)
        return l_matrix, u_matrix
    except ValueError as e:
        return str(e)

# Example matrix to test the function
matrix = [
    [4, 3, 2],
    [2, 1, 1],
    [6, 5, 4]
]

result = invoke_lu(matrix)
print(result)
