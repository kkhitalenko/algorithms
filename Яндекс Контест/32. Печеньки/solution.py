def get_count_of_children_satisfied(greed_factor, cookies_sizes):
    cookie_ind, greed_ind, result = 0, 0, 0
    while cookie_ind < len(cookies_sizes) and greed_ind < len(greed_factor):
        if greed_factor[greed_ind] <= cookies_sizes[cookie_ind]:
            result += 1
            cookie_ind += 1
        greed_ind += 1
    return result


if __name__ == '__main__':
    children = int(input())
    greed_factor = sorted(list(map(int, input().split())), reverse=True)
    cookies = int(input())
    cookies_sizes = sorted(list(map(int, input().split())), reverse=True)
    print(get_count_of_children_satisfied(greed_factor, cookies_sizes))
