class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


# ------- TASK 1 ------- #

def max_value_node(node):
    if node is None:
        return None
    current = node
    while current.right:  # go to the rightmost node
        current = current.right
    return current


# ------- TASK 2 ------- #

def min_value_node(node):
    if node is None:
        return None
    current = node
    while current.left:  # go to the leftmost node
        current = current.left
    return current

# ------- TASK 3 ------- #

def sum_tree(node):
    if node is None:
        return 0
    return node.val + sum_tree(node.left) + sum_tree(node.right)

# Test
if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)

    print("Max value:", max_value_node(root).val)
    print("Min value:", min_value_node(root).val)
    print("Sum of all values:", sum_tree(root))
