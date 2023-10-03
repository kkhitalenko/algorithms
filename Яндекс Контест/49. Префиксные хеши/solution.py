from typing import List


def print_prefix_hash(base, module, string, substring_limits: List[List[int]]):
    prefixes = [0, ]
    for i in range(1, len(string)+1):
        prefixes.append((prefixes[i-1] * base % module +
                         ord(string[i-1])) % module)
    for i in range(len(substring_limits)):
        start = substring_limits[i][0]
        end = substring_limits[i][1]
        hash = (prefixes[end] - (prefixes[start-1] *
                                 pow(base, end-start+1, module))) % module
        print(hash)


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    s = input()
    t = int(input())
    substring_limits = list(list(map(int, input().split())) for _ in range(t))
    print_prefix_hash(a, m, s, substring_limits)
