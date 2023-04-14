def binary_search(accumulations, price, left, right):
    if right <= left:
        return - 1
    mid = (left + right) // 2
    if accumulations[mid] < price:
        return binary_search(accumulations, price, mid + 1, right)
    elif accumulations[mid] >= price:
        if mid == 0:
            return 1
        elif accumulations[mid-1] < price:
            return mid + 1
        return binary_search(accumulations, price, left, mid)


if __name__ == '__main__':
    days = int(input())
    accumulations = list(map(int, input().split()))
    price = int(input())
    first_bike = binary_search(accumulations, price, 0, days)
    second_bike = binary_search(accumulations, price * 2, 0, days)
    print(first_bike, second_bike)
