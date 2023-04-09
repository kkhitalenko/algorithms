class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def is_correct_bracket_seq(stack, seq):
    open_brackets = ['(', '{', '[']
    if len(seq) == 0:
        return True
    if len(seq) % 2 != 0:
        return False
    for i in seq:
        if i in open_brackets:
            stack.push(i)
        elif len(stack.items) == 0:
            return False
        elif i == '}':
            if stack.items[-1] != '{':
                return False
            stack.pop()
        elif i == ')':
            if stack.items[-1] != '(':
                return False
            stack.pop()
        elif i == ']':
            if stack.items[-1] != '[':
                return False
            stack.pop()
    return True


if __name__ == '__main__':
    seq = input()
    stack = Stack()
    print(is_correct_bracket_seq(stack, seq))
