def sort(items):
    left, center, right = [], [], []
    pivot = 1
    for item in items:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            center.append(item)
        elif item > pivot:
            right.append(item)
    return left + center + right


if __name__ == '__main__':
    items_qty = int(input())
    items = list(map(int, input().split()))
    print(*sort(items))
