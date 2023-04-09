class StackIsEmptyException(Exception):
    pass


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_values = []

    def top(self):
        return self.items[-1]

    def push(self, item):
        if len(self.items) == 0:
            self.max_values.append(item)
        elif item > self.max_values[len(self.items)-1]:
            self.max_values.append(item)
        else:
            self.max_values.append(self.max_values[len(self.items)-1])
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise StackIsEmptyException
        self.max_values.pop()
        return self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            raise StackIsEmptyException
        return self.max_values[-1]


if __name__ == '__main__':
    n = int(input())
    stack = StackMaxEffective()
    for _ in range(n):
        try:
            command = input().split()
            if len(command) == 2:
                stack.push(int(command[1]))
            elif command[0] == 'pop':
                stack.pop()
            elif command[0] == 'get_max':
                print(stack.get_max())
        except StackIsEmptyException:
            if command[0] == 'get_max':
                print('None')
            elif command[0] == 'pop':
                print('error')
