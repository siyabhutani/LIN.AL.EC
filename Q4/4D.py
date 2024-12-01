#4D
def check_subspace(A, B):
    def linear_combo(vecs, target):
        n = len(vecs)
        l = len(target)
        valid = True
        for i in range(l):
            coeffs = [0] * n
            for j in range(n):
                coeffs[j] = vecs[j][i]
            total = 0
            for c in coeffs:
                total += c
            if total != target[i]:
                valid = False
                break
        return valid

    for a in A:
        if not linear_combo(B, a):
            return False
    return True

def is_subsp(S1, S2):
    return check_subspace(S1, S2)

# Example use case
S1 = [[1, 2], [2, 4]]
S2 = [[1, 0], [0, 1]]
print(is_subsp(S1, S2))  # Output: False
