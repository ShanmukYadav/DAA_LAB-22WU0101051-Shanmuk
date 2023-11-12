def interchange_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][i], matrix[i][n - i - 1] = matrix[i][n - i - 1], matrix[i][i]
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(interchange_diagonals(matrix))
