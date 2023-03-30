def num_to_binary(num: int) -> int:
    if num == 0:
        return 0
    result = ''
    while num != 0:
        result += str((num) % 2)
        num = (num) // 2
    return result[::-1]


print(num_to_binary(int(input())))
