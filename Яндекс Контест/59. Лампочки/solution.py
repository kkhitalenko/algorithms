class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def get_max_value(node):
    if node is not None:
        max_value = node.value
        left = get_max_value(node.left)
        right = get_max_value(node.right)
        if left is not None:
            max_value = max(left, max_value)
        if right is not None:
            max_value = max(right, max_value)
        return max_value


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert get_max_value(node4) == 3


if __name__ == '__main__':
    test()
