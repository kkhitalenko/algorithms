def find_anagram(words):
    anagram_indices = {}
    for index, word in enumerate(words):
        sorted_word = str(sorted(word))
        if sorted_word in anagram_indices:
            anagram_indices[sorted_word].append(index)
        else:
            anagram_indices[sorted_word] = [index]
    for i in anagram_indices.values():
        print(*i)


if __name__ == '__main__':
    n = int(input())
    find_anagram(input().split())
