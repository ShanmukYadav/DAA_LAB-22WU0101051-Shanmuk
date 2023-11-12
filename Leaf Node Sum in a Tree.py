class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def leaf_node_sum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.value
    return leaf_node_sum(root.left) + leaf_node_sum(root.right)

# Test the function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(leaf_node_sum(root))
