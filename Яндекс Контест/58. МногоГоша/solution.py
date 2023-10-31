def get_polynomial_hash(base, module, string):
    hash = 0
    power = 1
    for element in string[::-1]:
        hash = (hash + ord(element) * power) % module
        power = (power * base) % module
    return hash


def get_substrings(length, k, string):
    if len(string) < length:
        return 0

    hash = 0
    hash_module = 2 ** 64
    hash_base = 10 ** 9 + 7
    power = pow(hash_base, length - 1, hash_module)

    # Хеши подстрок и их вхождения
    substring_hashes = {}

    # Индексы подстрок, встречающиеся k раз
    required_substring_indices = []

    for i in range(len(string) - length + 1):
        if i == 0:
            substring = string[0:length]
            hash = get_polynomial_hash(hash_base, hash_module, substring)
        else:
            prev_hash = (ord(string[i - 1]) * power) % hash_module
            hash = (((hash - prev_hash) * hash_base) %
                    hash_module) + ord(string[i + length - 1])

        if hash in substring_hashes:
            substring_hashes[hash][1] += 1
        else:
            substring_hashes[hash] = [i, 1]

        if substring_hashes[hash][1] == k:
            required_substring_indices.append(substring_hashes[hash][0])

    return required_substring_indices


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(*get_substrings(n, k, s))
