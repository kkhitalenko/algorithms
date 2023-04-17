def get_flowerbed_borders(array):
    element = start_index = 0
    next_element = end_index = 1
    result = array[element]
    while next_element < n:
        item = array[next_element]
        changed = False
        if item[start_index] <= result[start_index]:
            result[start_index] = item[start_index]
            changed = True
        elif ((item[start_index] > result[start_index]) and
              (item[start_index] <= result[end_index])):
            if result[end_index] < item[end_index]:
                result[end_index] = item[end_index]
            changed = True
        if not changed:
            print(*result)
            result = item
        next_element += 1
    print(*result)


if __name__ == "__main__":
    n = int(input())
    array = []
    for _ in range(n):
        array.append(list(map(int, input().split())))
    array.sort()
    get_flowerbed_borders(array)
