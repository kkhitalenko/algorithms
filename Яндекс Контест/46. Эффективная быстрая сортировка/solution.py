import random


def quick_sort(data_list: list, left: int, right: int):
    if left >= right:
        return -1
    pivot = data_list[random.randint(left, right)]
    left_pointer, right_pointer = left, right
    while left_pointer <= right_pointer:
        while data_list[left_pointer] < pivot:
            left_pointer += 1
        while data_list[right_pointer] > pivot:
            right_pointer -= 1
        if left_pointer <= right_pointer:
            data_list[left_pointer], data_list[right_pointer] = \
                data_list[right_pointer], data_list[left_pointer]
            left_pointer += 1
            right_pointer -= 1
    quick_sort(data_list, left, right_pointer)
    quick_sort(data_list, left_pointer, right)


if __name__ == '__main__':
    members = int(input())
    data_list = []
    for _ in range(members):
        name, tasks, fine = input().split()
        data_list.append(list((-int(tasks), int(fine), name)))
    quick_sort(data_list, 0, members-1)
    for element in data_list:
        print(element[2])
