def is_power_of_four(number: int) -> bool:
    if number == 1:
        return True
    list = [4, ]
    while list[-1] < 10000:
        list.append((list[-1])*4)
    if number in list:
        return True
    return False


print(is_power_of_four(int(input())))
