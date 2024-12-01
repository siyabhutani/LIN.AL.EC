#5B
def invadj(matrix):
    size = len(matrix)
    if size != len(matrix[0]):
        return "Matrix is not square, so it cannot be inverted"
    
    det = determinant(matrix)
    if det == 0:
        return "Matrix is not invertible"
    
    adj = adjoint(matrix)
    inverse = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(adj[i][j] / det)
        inverse.append(row)
    return inverse

def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    result = 0
    for i in range(n):
        submatrix = []
        for j in range(1, n):
            subrow = []
            for k in range(n):
                if k != i:
                    subrow.append(matrix[j][k])
            submatrix.append(subrow)
        result += ((-1) ** i) * matrix[0][i] * determinant(submatrix)
    return result

def adjoint(matrix):
    n = len(matrix)
    adj = []
    for i in range(n):
        row = []
        for j in range(n):
            submatrix = []
            for k in range(n):
                if k != i:
                    subrow = []
                    for l in range(n):
                        if l != j:
                            subrow.append(matrix[k][l])
                    submatrix.append(subrow)
            cofactor = ((-1) ** (i + j)) * determinant(submatrix)
            row.append(cofactor)
        adj.append(row)
    
    adj_t = []
    for i in range(n):
        trans_row = []
        for j in range(n):
            trans_row.append(adj[j][i])
        adj_t.append(trans_row)
    return adj_t
