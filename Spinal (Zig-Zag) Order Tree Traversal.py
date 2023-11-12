from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_spiral(root):
    if root is None:
        return

    current_level = deque()
    next_level = deque()

    current_level.append(root)

    left_to_right = True

    while current_level:
        node = current_level.pop()
        print(node.value, end=' ')

        if left_to_right:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        else:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)

        if not current_level:
            left_to_right = not left_to_right
            current_level, next_level = next_level, current_level
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print_spiral(root)
