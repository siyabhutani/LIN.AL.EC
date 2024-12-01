#3G
def compute_PLU(mat):
    n = len(mat)
    L = [[0 if i != j else 1 for j in range(n)] for i in range(n)]
    U = [[mat[i][j] for j in range(n)] for i in range(n)]
    P = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for k in range(n):
        pivot = k
        for i in range(k + 1, n):
            if abs(U[i][k]) > abs(U[pivot][k]):
                pivot = i
        
        if pivot != k:
            U[k], U[pivot] = U[pivot], U[k]
            P[k], P[pivot] = P[pivot], P[k]
            L[k][:k], L[pivot][:k] = L[pivot][:k], L[k][:k]
        
        for i in range(k + 1, n):
            factor = U[i][k] / U[k][k]
            L[i][k] = factor
            for j in range(k, n):
                U[i][j] -= factor * U[k][j]

    return P, L, U

# Example usage
matrix = [
    [2, 3, 1],
    [4, 7, 5],
    [6, 18, 22]
]

P, L, U = compute_PLU(matrix)
print("P:", P)
print("L:", L)
print("U:", U)
