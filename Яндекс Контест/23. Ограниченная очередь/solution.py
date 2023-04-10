class QueueIsEmptyException(Exception):
    pass


class QueueIsOverflowException(Exception):
    pass


class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_size_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def push(self, x):
        if self.size == self.max_size_n:
            raise QueueIsOverflowException
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.max_size_n
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise QueueIsEmptyException
        last_number = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size_n
        self.size -= 1
        return last_number

    def peek(self):
        return self.queue[self.head]


if __name__ == '__main__':
    commands = int(input())
    queue_size = int(input())
    queue = MyQueueSized(queue_size)
    for _ in range(commands):
        try:
            command = input().split()
            if len(command) == 2:
                queue.push(int(command[1]))
            elif command[0] == 'size':
                print(queue.size)
            else:
                print(getattr(queue, command[0])())
        except QueueIsOverflowException:
            print('error')
        except QueueIsEmptyException:
            print('None')
