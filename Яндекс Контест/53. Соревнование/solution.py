def get_max_length(n, numbers):
    if n < 2:
        return 0

    indices_of_prefix_amounts = {}
    prefix_amount, max_len = 0, 0

    for i in range(n):
        if numbers[i] == 0:
            prefix_amount -= 1
        else:
            prefix_amount += 1

        if prefix_amount == 0:
            max_len = i + 1
        elif prefix_amount in indices_of_prefix_amounts:
            max_len = max(max_len,
                          i - indices_of_prefix_amounts[prefix_amount])
        else:
            indices_of_prefix_amounts[prefix_amount] = i

    return max_len


if __name__ == '__main__':
    n = int(input())
    numbers = [int(i) for i in input().split()]
    print(get_max_length(n, numbers))
