def merge(array, lf, mid, rg):
    result = []
    left_arr = array[lf:mid]
    right_arr = array[mid:rg]
    left_index, right_index = 0, 0
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] <= right_arr[right_index]:
            result.append(left_arr[left_index])
            left_index += 1
        else:
            result.append(right_arr[right_index])
            right_index += 1
        if right_index == len(right_arr):
            result += left_arr[left_index:]
            break
        if left_index == len(left_arr):
            result += right_arr[right_index:]
            break
    return result


def merge_sort(array, begin, end):
    if end - begin > 1:
        mid = (begin + end) // 2
        merge_sort(array, begin, mid)
        merge_sort(array, mid, end)
        array[begin:end] = merge(array, begin, mid, end)
