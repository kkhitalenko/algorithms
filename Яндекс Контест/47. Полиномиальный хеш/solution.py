def get_polynomial_hash(base, module, string):
    hash = 0
    power = 1
    for element in string[::-1]:
        hash = (hash + ord(element) * power) % module
        power = (power * base) % module
    return hash


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    s = input()
    print(get_polynomial_hash(a, m, s))
