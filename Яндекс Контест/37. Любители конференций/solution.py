def get_most_active_participient_uni(ids):
    students_in_uni = {}
    for id in ids:
        if id in students_in_uni:
            students_in_uni[id] += 1
        else:
            students_in_uni[id] = 1
    return (sorted(students_in_uni.items(), key=lambda item: item[1],
                   reverse=True))


if __name__ == '__main__':
    students = int(input())
    ids = list(map(int, input().split()))
    k = int(input())
    result = list(get_most_active_participient_uni(ids))
    for i in range(k):
        print(result[i][0], end=' ')
