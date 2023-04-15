def bubble_sort(array):
    array_was_initially_sorted = True
    while True:
        array_changed = False
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                array_changed = True
                array_was_initially_sorted = False

        if array_was_initially_sorted:
            print(*array)

        if array_changed:
            print(*array)
        else:
            break


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().split()))
    bubble_sort(array)
