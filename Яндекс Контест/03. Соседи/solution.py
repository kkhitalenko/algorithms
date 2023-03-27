from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []
    max_column_index = len(matrix[row])-1
    max_row_index = len(matrix) - 1
    my_row = matrix[row]
    if max_column_index != 0:
        if col == 0:
            result.append(my_row[1])
        elif col == max_column_index:
            result.append(my_row[col - 1])
        else:
            result.append(my_row[col - 1])
            result.append(my_row[col + 1])
    if max_row_index != 0:
        if row == 0:
            upper_row = matrix[row+1]
            result.append(upper_row[col])
        elif row == max_row_index:
            lower_row = matrix[row-1]
            result.append(lower_row[col])
        else:
            upper_row = matrix[row+1]
            lower_row = matrix[row-1]
            result.append(lower_row[col])
            result.append(upper_row[col])
    return sorted(result)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


if __name__ == '__main__':
    matrix, row, col = read_input()
    print(*get_neighbours(matrix, row, col))
