from math import factorial


def get_qty_of_different_search_trees(n):
    return int(factorial(2 * n) / (factorial(n) * factorial(n + 1)))


if __name__ == '__main__':
    n = int(input())
    print(get_qty_of_different_search_trees(n))
