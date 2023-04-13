def get_bracket_sequence(n, left=0, right=0, prefix=''):
    if left == right == n:
        print(prefix)
    else:
        if left < n:
            get_bracket_sequence(n, left + 1, right, prefix + '(')
        if right < left:
            get_bracket_sequence(n, left, right + 1, prefix + ')')


if __name__ == '__main__':
    n = int(input())
    get_bracket_sequence(n)
