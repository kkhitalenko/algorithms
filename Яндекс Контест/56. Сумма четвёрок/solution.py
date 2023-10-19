def get_sum_of_fours(num, array):
    array_length = len(array)
    array.sort()

    # суммы пар элементов и индексы этих элементов в отсортированном массиве
    sum_of_twos = {}
    for i in range(array_length - 1):
        for j in range(i + 1, array_length):
            sum_of_curr_twos = array[i] + array[j]
            if sum_of_curr_twos in sum_of_twos:
                sum_of_twos[sum_of_curr_twos].append((i, j))
            else:
                sum_of_twos[sum_of_curr_twos] = [(i, j)]

    res = set()
    for i in range(2, array_length - 1):
        for j in range(i + 1, array_length):
            expected_sum = num - array[i] - array[j]
            if expected_sum in sum_of_twos:
                for pair in sum_of_twos[expected_sum]:
                    if pair[1] < i:
                        res.add((array[pair[0]], array[pair[1]],
                                 array[i], array[j]))
    return sorted(list(res))


if __name__ == '__main__':
    n = int(input())
    s = int(input())
    array = [int(i) for i in input().split()]
    res = get_sum_of_fours(s, array)
    print(len(res))
    for four in res:
        print(*four)
