def factorize(number):
    result = []
    divider = 2
    while number >= divider ** 2:
        if number % divider == 0:
            result.append(divider)
            number //= divider
        else:
            divider += 1
    if number > 1:
        result.append(number)
    return result


if __name__ == '__main__':
    number = int(input())
    print(" ".join(map(str, factorize(number))))
