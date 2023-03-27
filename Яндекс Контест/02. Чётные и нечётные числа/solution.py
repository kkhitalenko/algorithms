def check_parity(a: int, b: int, c: int) -> str:
    if (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0):
        return 'WIN'
    elif (a % 2 != 0) and (b % 2 != 0) and (c % 2 != 0):
        return 'WIN'
    else:
        return 'FAIL'


if __name__ == '__main__':
    a, b, c = map(int, input().strip().split())
    print(check_parity(a, b, c))
