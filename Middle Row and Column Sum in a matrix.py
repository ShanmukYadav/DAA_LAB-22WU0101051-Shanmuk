def middle_row_col_sum(matrix):
    n = len(matrix)
    mid = n // 2

    # Calculate the sum of the middle row
    row_sum = sum(matrix[mid])

    # Calculate the sum of the middle column
    col_sum = sum(matrix[i][mid] for i in range(n))

    return row_sum, col_sum

# Test the function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_sum, col_sum = middle_row_col_sum(matrix)
print(f"Sum of the middle row: {row_sum}")
print(f"Sum of the middle column: {col_sum}")
