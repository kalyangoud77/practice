matrix = ([1, 2, 3, 4], [4, 1, 0, 1], [7, 2, 1, 3], [4, 5, 1, 0])

m = 4
n = 4

def max_path(matrix):

    result = -1

    for i in range(m):
        result = max(result, matrix[0][1])

    for i in range(1, n):
        result = -1

    for j in range(m):

        if (j > 0 and j < m - 1):

            matrix[i][j] += max(matrix[i - 1][j], max(matrix[i - 1][j - 1], matrix[i - 1][j + 1]))

        elif (j > 0):

            matrix[i][j] += max(matrix[i - 1][j], matrix[i - 1][j - 1])

        elif (j < m - 1):

            matrix[i][j] += max(matrix[i - 1][j], matrix[i - 1][j + 1])

        result = max(matrix[i][j], result)
    return result

print(max_path(matrix))
