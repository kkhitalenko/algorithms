def transpose(matrix, rows, columns):
    trans_matrix = []
    for _ in range(columns):
        trans_row = [0] * rows
        trans_matrix.append(trans_row)
    for column in range(columns):
        for row in range(rows):
            trans_matrix[column][row] = matrix[row][column]
    return trans_matrix


if __name__ == '__main__':
    rows, columns = int(input()), int(input())
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    trans_matrix = transpose(matrix, rows, columns)
    for row in trans_matrix:
        print(*row)
