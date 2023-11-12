def sort_matrix_and_replace_diagonals(matrix):
    # Flatten the matrix and sort it
    flat_list = [item for sublist in matrix for item in sublist]
    flat_list.sort()

    # Reshape the sorted list back into a matrix
    sorted_matrix = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(flat_list[i * len(matrix) + j])
        sorted_matrix.append(row)

    # Replace the diagonals with zeros
    n = len(sorted_matrix)
    for i in range(n):
        sorted_matrix[i][i] = 0
        sorted_matrix[i][n - i - 1] = 0

    return sorted_matrix

# Test the function
matrix = [[37, 29, 20], [4, 9, 13], [18, 2, 34]]
print(sort_matrix_and_replace_diagonals(matrix))
