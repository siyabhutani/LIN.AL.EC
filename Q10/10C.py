#10C
def transpose_matrix(mat):
    t_mat = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return t_mat

def multiply_matrices(x, y):
    prod = [[0] * len(y[0]) for _ in range(len(x))]
    for r in range(len(x)):
        for c in range(len(y[0])):
            for k in range(len(y)):
                prod[r][c] += x[r][k] * y[k][c]
    return prod

def eigen_decomp(sqr_mat):
    vals = [row[:] for row in sqr_mat]
    eig_vec = [[1 if i == j else 0 for j in range(len(vals))] for i in range(len(vals))]
    for _ in range(50):
        for r in range(len(vals)):
            for c in range(len(vals)):
                if r != c:
                    diff = (vals[c][c] - vals[r][r])
                    if diff != 0:
                        angle = (2 * vals[r][c]) / diff
                        t = 1 / (abs(angle) + (angle ** 2 + 1) ** 0.5)
                        cos_t = 1 / (1 + t ** 2) ** 0.5
                        sin_t = t * cos_t
                        for i in range(len(vals)):
                            temp = cos_t * vals[r][i] - sin_t * vals[c][i]
                            vals[c][i] = sin_t * vals[r][i] + cos_t * vals[c][i]
                            vals[r][i] = temp
                        for i in range(len(vals)):
                            temp = cos_t * vals[i][r] - sin_t * vals[i][c]
                            vals[i][c] = sin_t * vals[i][r] + cos_t * vals[i][c]
                            vals[i][r] = temp
                        for i in range(len(vals)):
                            temp = cos_t * eig_vec[i][r] - sin_t * eig_vec[i][c]
                            eig_vec[i][c] = sin_t * eig_vec[i][r] + cos_t * eig_vec[i][c]
                            eig_vec[i][r] = temp
    eig_vals = [vals[i][i] for i in range(len(vals))]
    return eig_vals, eig_vec

def decompose_svd(mat):
    t_mat = transpose_matrix(mat)
    at_a = multiply_matrices(t_mat, mat)
    eig_vals, eig_vec_u = eigen_decomp(at_a)
    s_vals = [val ** 0.5 if val > 0 else 0 for val in eig_vals]
    s_diag = [[s_vals[i] if i == j else 0 for j in range(len(s_vals))] for i in range(len(mat))]
    aa_t = multiply_matrices(mat, t_mat)
    _, eig_vec_v = eigen_decomp(aa_t)
    return eig_vec_v, s_diag, transpose_matrix(eig_vec_u)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

left_singular, singular_diag, right_singular = decompose_svd(matrix)

print("Left Singular Vectors:")
for row in left_singular:
    print(row)
print("Singular Values:")
for row in singular_diag:
    print(row)
print("Right Singular Vectors:")
for row in right_singular:
    print(row)
