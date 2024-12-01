#3D
def span_dimension(vectors):
    matrix = []
    for vec in vectors:
        matrix.append(vec[:])
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][i] != 0:
                factor = matrix[j][i] / matrix[i][i]
                for k in range(len(matrix[i])):
                    matrix[j][k] -= factor * matrix[i][k]
    rank = 0
    for row in matrix:
        if any(x != 0 for x in row):
            rank += 1
    return rank

def find_basis(vectors):
    results = []
    for v in vectors:
        temp_set = results + [v]
        if span_dimension(temp_set) > span_dimension(results):
            results.append(v)
    return results

# Example Usage
S = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
dimension = span_dimension(S)
basis = find_basis(S)
print(dimension)
print(basis)
