def get_longest_word(text: str) -> str:
    longest_word = ''
    words = text.split()
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


if __name__ == '__main__':
    _ = input()
    text = input()
    print(get_longest_word(text))
    print(len(get_longest_word(text)))
