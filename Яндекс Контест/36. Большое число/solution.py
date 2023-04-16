def is_first_element_of_number_is_bigger(number_1: str, number_2: str, i=0):
    number_1_max_index = len(number_1) - 1
    number_2_max_index = len(number_2) - 1
    min_max_index = min(number_1_max_index, number_2_max_index)
    max_max_index = max(number_1_max_index, number_2_max_index)
    while i <= min_max_index:
        if number_1[i] > number_2[i]:
            return True
        elif number_1[i] < number_2[i]:
            return False
        elif number_1[i] == number_2[i]:
            return is_first_element_of_number_is_bigger(number_1, number_2,
                                                        i + 1)
    while i <= max_max_index:
        if number_1_max_index > number_2_max_index:
            number_1 = number_1[min_max_index + 1:]
        else:
            number_2 = number_2[min_max_index + 1:]
        return is_first_element_of_number_is_bigger(number_1, number_2)


def biggest_number(array, bigger):
    for i in range(1, n):
        item_to_insert = array[i]
        item_to_insert_index = i
        while (
            item_to_insert_index > 0
            and bigger(item_to_insert, array[item_to_insert_index-1])
        ):
            array[item_to_insert_index] = array[item_to_insert_index-1]
            item_to_insert_index -= 1
        array[item_to_insert_index] = item_to_insert
    return ''.join(array)


if __name__ == '__main__':
    n = int(input())
    array = list(input().split())
    print(biggest_number(array, is_first_element_of_number_is_bigger))
