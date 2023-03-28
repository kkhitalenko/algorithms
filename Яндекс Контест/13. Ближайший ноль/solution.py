def get_nearest_null(n: int, house_numbers: list) -> list:
    distance_to_nearest_null = [0] * n
    if house_numbers[0] != 0:
        distance_to_nearest_null[0] = 1
    for index, value in enumerate(house_numbers):
        if value != 0 and index != 0:
            distance_to_nearest_null[index] = (
                distance_to_nearest_null[index-1]+1
            )
    for index, value in enumerate(house_numbers[::-1]):
        if (
            value != 0 and index != 0
            and distance_to_nearest_null[n-index-1] > (
             distance_to_nearest_null[n-index]
            )
        ):
            distance_to_nearest_null[n-index-1] = (
                distance_to_nearest_null[n-index]+1
            )
    first_null_index = -1
    while first_null_index == -1:
        first_null_index = distance_to_nearest_null.index(0)
    for index, value in enumerate(house_numbers[::-1][:first_null_index]):
        if index != 0:
            distance_to_nearest_null[first_null_index-index] = (
                distance_to_nearest_null[first_null_index-index+1]+1
            )
    if house_numbers[0] != 0:
        distance_to_nearest_null[0] = distance_to_nearest_null[1]+1
    return distance_to_nearest_null


if __name__ == '__main__':
    n = int(input())
    house_numbers = list(map(int, input().split()))
    result = get_nearest_null(n, house_numbers)
    print(*result)
