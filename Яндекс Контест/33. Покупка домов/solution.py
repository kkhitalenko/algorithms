def get_max_number_of_houses_to_buy(budget, prices):
    res = 0
    total__budget = 0
    prices.sort()
    for price in prices:
        if price + total__budget <= budget:
            res += 1
            total__budget += price
        else:
            return res
    return res


if __name__ == '__main__':
    houses, budget = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    print(get_max_number_of_houses_to_buy(budget, prices))
