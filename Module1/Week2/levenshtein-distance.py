def find_min_distance(source_str, target_str):
    """
    1. Create matrix(row x col)
    2. Fill first row and column
    3. Fill matrix based on previous edits
    4. Return final element (Levenshtein distance)
    """
    col_num = len(target_str) + 1
    row_num = len(source_str) + 1
    matrx = [[0] * col_num for _ in range(row_num)]

    for i in range(row_num):
        for j in range(col_num):
            if i == 0 and j == 0:
                matrx[i][j] = 0
            elif i == 0:
                matrx[i][j] += matrx[i][j - 1] + 1
            elif j == 0:
                matrx[i][j] = matrx[i - 1][j] + 1

            elif source_str[i - 1] == target_str[j - 1]:
                matrx[i][j] = matrx[i - 1][j - 1]
            else:
                matrx[i][j] = 1 + min(
                    matrx[i - 1][j], matrx[i][j - 1], matrx[i - 1][j - 1]
                )
    return matrx[row_num - 1][col_num - 1]
