#3A
def get_vector_length(vector):
    length = 0
    for _ in vector:
        length += 1
    return length

def get_matrix_dimensions(matrix):
    num_rows = 0
    for _ in matrix:
        num_rows += 1
    num_cols = 0
    for _ in matrix[0]:
        num_cols += 1
    return num_rows, num_cols

def calculate_matrix_rank(matrix):
    total_rows = len(matrix)
    total_cols = len(matrix[0])
    current_step = 0
    while current_step < min(total_rows, total_cols):
        if matrix[current_step][current_step] == 0:
            for swap_index in range(current_step + 1, total_rows):
                if matrix[swap_index][current_step] != 0:
                    matrix[current_step], matrix[swap_index] = matrix[swap_index], matrix[current_step]
                    break
        if matrix[current_step][current_step] != 0:
            for target_row in range(current_step + 1, total_rows):
                scale_factor = matrix[target_row][current_step] / matrix[current_step][current_step]
                for target_col in range(total_cols):
                    matrix[target_row][target_col] -= scale_factor * matrix[current_step][target_col]
        current_step += 1
    rank = 0
    for row in matrix:
        if any(element != 0 for element in row):
            rank += 1
    return rank

def calculate_matrix_nullity(matrix):
    rows, cols = get_matrix_dimensions(matrix)
    return cols - calculate_matrix_rank(matrix)

# Example usage
example_vector = [1, 2, 3]
example_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

vector_length_result = get_vector_length(example_vector)
matrix_size_result = get_matrix_dimensions(example_matrix)
matrix_rank_result = calculate_matrix_rank([row[:] for row in example_matrix])  # Copy matrix to avoid mutation
matrix_nullity_result = calculate_matrix_nullity([row[:] for row in example_matrix])

print("Length of Vector:", vector_length_result)
print("Dimensions of Matrix (rows, columns):", matrix_size_result)
print("Rank of the Matrix:", matrix_rank_result)
print("Nullity of the Matrix:", matrix_nullity_result)

