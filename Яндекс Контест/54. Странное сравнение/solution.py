def strange_hash_function(s):
    """Возвращает строку, в которой на месте каждого элемента указан индекс его
    первого вхождения."""

    hash = []
    hash_table = {}
    for index, character in enumerate(s):
        if character not in hash_table:
            hash.append(index)
            hash_table[character] = index
        else:
            hash.append(hash_table[character])
    return str(hash)


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    if strange_hash_function(s1) == strange_hash_function(s2):
        print('YES')
    else:
        print('NO')
