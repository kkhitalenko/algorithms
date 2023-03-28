def solution(node, elem):
    index = -1
    while index != 10000:
        if node is None:
            return -1
        elif elem == node.value:
            return index + 1
        else:
            node = node.next_item
            index += 1
