import random
from string import ascii_lowercase


def get_random_str():
    len_str = random.randint(1, 1000)
    string = ''.join(random.choice(ascii_lowercase) for _ in range(len_str))
    return string


def get_polynomial_hash(base, module, string):
    hash = 0
    power = 1
    for element in string[::-1]:
        hash = (hash + ord(element) * power) % module
        power = (power * base) % module
    return hash


if __name__ == '__main__':
    a = 1000
    m = 123987123
    hashes = {}
    while True:
        random_str = get_random_str()
        random_str_hash = get_polynomial_hash(a, m, random_str)
        if not hashes.get(random_str_hash):
            hashes[random_str_hash] = random_str
        else:
            print(random_str, hashes[random_str_hash])
            break
