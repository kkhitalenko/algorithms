class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

# Рекурсивный способ, пойдёт до 1000
# import sys

# def is_bst(node, min_value=-sys.maxsize, max_value=sys.maxsize):
#     if node is None:
#         return True
#     if node.value < min_value or node.value > max_value:
#         return False
#     left = is_bst(node.left, min_value, node.value-1)
#     right = is_bst(node.right, node.value+1, max_value)
#     return left and right


def is_bst(node):
    prev = None
    while node is not None:
        if node.left is None:
            if prev is not None and prev.value >= node.value:
                return False
            prev = node
            node = node.right
        else:
            cur_node = node.left
            while cur_node.right is not None and cur_node.right is not node:
                cur_node = cur_node.right
            if cur_node.right is None:
                cur_node.right = node
                node = node.left
            else:
                cur_node.right = None
                if prev is not None and prev.value >= node.value:
                    return False
                prev = node
                node = node.right
    return True


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert is_bst(node5)
    node2.value = 5
    assert not is_bst(node5)


if __name__ == '__main__':
    test()
