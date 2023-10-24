# подумать ещё, не проходит по времени при больших объёмах данных
# ограничение по времени 0.058 секунд

def get_median(n, m, north, south):
    max_median_ind = (n + m) // 2
    sorted_list = []
    i, j = 0, 0
    while len(sorted_list) <= max_median_ind and i < n and j < m:
        if north[i] <= south[j]:
            sorted_list.append(north[i])
            i += 1
        else:
            sorted_list.append(south[j])
            j += 1
    sorted_list += north[i:] + south[j:]
    if (n + m) % 2 != 0:
        return sorted_list[max_median_ind]
    else:
        return (sorted_list[max_median_ind-1] + sorted_list[max_median_ind])/2

if __name__ == '__main__':
    n, m = int(input()), int(input())
    north = list(map(int, input().split()))
    south = list(map(int, input().split()))
    print(get_median(n, m, north, south))
