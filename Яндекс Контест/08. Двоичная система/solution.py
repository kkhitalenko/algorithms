def add(a, b):
    result = ''
    remainder = 0
    max_size = max(len(a), len(b))
    a += '0' * (max_size - len(a))
    b += '0' * (max_size - len(b))
    for i in zip(a, b):
        value = int(i[0]) + int(i[1]) + remainder
        remainder = value // 2
        result += str(value % 2)
    if remainder == 1:
        result += '1'
    return result[::-1]


if __name__ == '__main__':
    a, b = input(), input()
    print(''.join(map(str, add(a[::-1], b[::-1]))))
