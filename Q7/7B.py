#7B
def compute_determinant(matrix):
    def plu_decomposition(mat):
        n = len(mat)
        perm = list(range(n))
        for i in range(n - 1):
            pivot = i
            for j in range(i + 1, n):
                if abs(mat[j][i]) > abs(mat[pivot][i]):
                    pivot = j
            if pivot != i:
                perm[i], perm[pivot] = perm[pivot], perm[i]
                mat[i], mat[pivot] = mat[pivot], mat[i]
            for j in range(i + 1, n):
                factor = mat[j][i] / mat[i][i]
                for k in range(i, n):
                    mat[j][k] -= factor * mat[i][k]
                mat[j][i] = factor
        return mat, perm

    def determinant_from_plu(decomp, permute):
        swaps = sum(1 for i in range(len(permute)) if permute[i] != i)
        sign = (-1) ** swaps
        diag_prod = 1
        for i in range(len(decomp)):
            diag_prod *= decomp[i][i]
        return sign * diag_prod

    lu, perm = plu_decomposition(matrix)
    return determinant_from_plu(lu, perm)


# Example usage
matrix = [
    [2, 1, 1],
    [1, 3, 2],
    [1, 0, 0]
]

result = compute_determinant(matrix)
print(result)
