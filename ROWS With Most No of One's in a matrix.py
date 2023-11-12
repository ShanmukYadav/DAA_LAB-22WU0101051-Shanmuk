def rows_with_most_ones(matrix):
    max_count = 0
    rows = []

    for i in range(len(matrix)):
        count = matrix[i].count(1)

        if count > max_count:
            max_count = count
            rows = [i]
        elif count == max_count:
            rows.append(i)

    return rows

matrix = [[0, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 1], [1, 0, 0, 1]]
print(rows_with_most_ones(matrix))
