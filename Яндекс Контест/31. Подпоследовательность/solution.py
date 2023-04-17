def is_subsequence(s, t):
    if len(s) == 0:
        return True
    if len(s) > len(t):
        return False

    s_index = 0
    for t_index in range(len(t)):
        if s[s_index] == t[t_index]:
            s_index += 1
            if s_index == len(s):
                return True
    return False


if __name__ == '__main__':
    s = input()
    t = input()
    print(is_subsequence(s, t))
