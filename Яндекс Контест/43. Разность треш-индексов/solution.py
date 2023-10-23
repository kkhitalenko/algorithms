def get_difference(squares, k):
    squares.sort()
    min_dif, max_dif = 0, squares[-1] - squares[0]
    while min_dif < max_dif:
        mid = (min_dif + max_dif) // 2
        left = 0
        count = 0
        for right in range(len(squares)):
            while squares[right] - squares[left] > mid:
                left += 1
            count += right - left
        if count >= k:
            max_dif = mid
        else:
            min_dif = mid + 1
    return min_dif


if __name__ == '__main__':
    islands = int(input())
    squares = list(map(int, input().split()))
    k = int(input())
    print(get_difference(squares, k))
