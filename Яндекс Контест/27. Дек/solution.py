class DequeIsEmptyException(Exception):
    pass


class DequeIsOverflowException(Exception):
    pass


class Deque:
    def __init__(self, max_deque_size):
        self.deque = [None] * max_deque_size
        self.max_deque_size = max_deque_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, value):
        if self.size != self.max_deque_size:
            self.deque[self.tail] = value
            self.tail = (self.tail + 1) % self.max_deque_size
            self.size += 1
        else:
            raise DequeIsOverflowException

    def push_front(self, value):
        if self.size != self.max_deque_size:
            self.deque[self.head-1] = value
            self.head = (self.head - 1) % self.max_deque_size
            self.size += 1
        else:
            raise DequeIsOverflowException

    def pop_back(self):
        if self.size != 0:
            deleted_element = self.deque[self.tail-1]
            self.deque[self.tail-1] = None
            self.tail = (self.tail - 1) % self.max_deque_size
            self.size -= 1
            return deleted_element
        raise DequeIsEmptyException

    def pop_front(self):
        if self.size != 0:
            deleted_element = self.deque[self.head]
            self.deque[self.head] = None
            self.head = (self.head + 1) % self.max_deque_size
            self.size -= 1
            return deleted_element
        raise DequeIsEmptyException


if __name__ == '__main__':
    commands_quantity = int(input())
    max_deque_size = int(input())
    deque = Deque(max_deque_size)
    for _ in range(commands_quantity):
        try:
            command = input().split()
            if len(command) == 1:
                print(getattr(deque, command[0])())
            else:
                getattr(deque, command[0])(command[1])
        except (DequeIsEmptyException, DequeIsOverflowException):
            print('error')
