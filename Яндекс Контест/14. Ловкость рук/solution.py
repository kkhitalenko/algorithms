def get_result(keys_pressable: int, number_list: list) -> int:
    count = 0
    for i in range(1, 10):
        if 0 < number_list.count(i) <= keys_pressable * 2:
            count += 1
    return count


if __name__ == '__main__':
    keys_pressable = int(input())
    number_list = []
    for _ in range(4):
        number = input()
        for i in number:
            if i != '.':
                number_list.append(int(i))
            else:
                number_list.append(i)
    print(get_result(keys_pressable, number_list))
