phone_keyboard_dict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def get_combinations(numbers, prefix=''):
    if not numbers:
        print(prefix, end=' ')
        return
    for character in phone_keyboard_dict[numbers[0]]:
        prefix += character
        get_combinations(numbers[1:], prefix)
        prefix = prefix[:-1]


if __name__ == '__main__':
    numbers = input()
    get_combinations(numbers)
