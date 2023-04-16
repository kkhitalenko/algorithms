def get_flowerbed_borders(array, element=0, next_element=1, start=0, end=1):
    result = array[element]
    while next_element < n:
        item = array[next_element]
        changed = False
        if item[start] <= result[start]:
            result[start] = item[start]
            changed = True
        elif (item[start] > result[start]) and (item[start] <= result[end]):
            if result[end] < item[end]:
                result[end] = item[end]
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
