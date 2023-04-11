class QueueIsEmptyException(Exception):
    pass


class ListQueue:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.size = 0

    def get(self):
        if self.size == 0:
            raise QueueIsEmptyException
        elif self.size == 1:
            queue_head = self.head
            self.head == self.Node()
            self.tail == self.Node()
            self.size -= 1
            return queue_head
        elif self.size == 2:
            queue_head = self.head
            self.head = self.tail
            self.size -= 1
            return queue_head
        else:
            queue_head = self.head
            self.head = self.tail.next.next
            self.tail.next = self.head
            self.size -= 1
            return queue_head

    def put(self, x):
        if self.size == 0:
            self.head = self.Node(value=x)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value=x)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.size += 1

    def __str__(self):
        return self.value


if __name__ == '__main__':
    commands = int(input())
    list_queue = ListQueue()
    for _ in range(commands):
        try:
            command = input().split()
            if len(command) == 2:
                list_queue.put(int(command[1]))
            elif command[0] == 'size':
                print(list_queue.size)
            elif command[0] == 'get':
                print(list_queue.get())
        except QueueIsEmptyException:
            print('error')
