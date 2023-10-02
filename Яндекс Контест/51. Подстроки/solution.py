def get_length_of_largest_substring(string):
    characters = []
    start, end, max_len = 0, 0, 0
    while end < len(string):
        if string[end] not in characters:
            characters.append(string[end])
            end += 1
            if end - start > max_len:
                max_len = end - start
        else:
            characters.remove(string[start])
            start += 1
    return max_len


if __name__ == '__main__':
    print(get_length_of_largest_substring(input()))
