class StackIsEmptyException(Exception):
    pass


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise StackIsEmptyException
        self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            raise StackIsEmptyException
        return max(self.items)


if __name__ == '__main__':
    n = int(input())
    stack = StackMax()
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
