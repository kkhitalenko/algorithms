def get_excessive_letter(shorter: str, longer: str) -> str:
    for i in longer:
        if i not in shorter:
            return i
    shorter_dict = dict()
    for j in shorter:
        if j not in shorter_dict:
            shorter_dict[j] = 1
        else:
            shorter_dict[j] += 1
    longer_dict = dict()
    for i in longer:
        if i not in longer_dict:
            longer_dict[i] = 1
        else:
            longer_dict[i] += 1
    for j in shorter_dict:
        if shorter_dict[j] != longer_dict[j]:
            return j


if __name__ == '__main__':
    shorter = input()
    longer = input()
    print(get_excessive_letter(shorter, longer))
