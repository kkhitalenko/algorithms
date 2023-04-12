class Stack:
    def __init__(self):
        self.items = []
        self.operations = {
            '+': lambda a, b: b + a,
            '-': lambda a, b: b - a,
            '*': lambda a, b: b * a,
            '/': lambda a, b: b // a
        }

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


if __name__ == '__main__':
    input_data = input()
    stack = Stack()
    for element in input_data.split():
        if element in stack.operations:
            stack.push(stack.operations[element](stack.pop(), stack.pop()))
        else:
            stack.push(int(element))
    print(stack.items[-1])
