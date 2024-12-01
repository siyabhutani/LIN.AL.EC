#5A
def invert_matrix(matrix):
    size = len(matrix)

    # Check if the matrix is square
    for row in matrix:
        if len(row) != size:
            return "Matrix must be square."

    # Augment matrix with identity
    augmented = [matrix[row][:] + [1 if row == col else 0 for col in range(size)] for row in range(size)]

    # Perform row reduction
    for diag in range(size):
        # Find the pivot row
        pivot_row = diag
        for row in range(diag + 1, size):
            if abs(augmented[row][diag]) > abs(augmented[pivot_row][diag]):
                pivot_row = row
        if augmented[pivot_row][diag] == 0:
            return "Matrix is not invertible."

        # Swap rows to bring the pivot to the diagonal
        if pivot_row != diag:
            augmented[diag], augmented[pivot_row] = augmented[pivot_row], augmented[diag]

        # Scale the pivot row to make the pivot element 1
        pivot_element = augmented[diag][diag]
        for col in range(2 * size):
            augmented[diag][col] /= pivot_element

        # Eliminate the column entries above and below the pivot
        for row in range(size):
            if row != diag:
                factor = augmented[row][diag]
                for col in range(2 * size):
                    augmented[row][col] -= factor * augmented[diag][col]

    # Extract the inverse matrix from the augmented matrix
    inverse = [row[size:] for row in augmented]
    return inverse


# Example usage
matrix_to_invert = [
    [4, 7],
    [2, 6]
]

result = invert_matrix(matrix_to_invert)
if isinstance(result, str):
    print(result)
else:
    print("Inverse of the matrix:")
    for row in result:
        print(row)
