# Experiment 15: Binary Search Tree for student register numbers
# Rule: smaller numbers go LEFT, bigger numbers go RIGHT

class Node:
    def __init__(self, number):
        self.number = number
        self.left = None
        self.right = None


def insert(node, number):
    # Empty spot found: place the new student here
    if node is None:
        return Node(number)

    if number < node.number:
        node.left = insert(node.left, number)
    elif number > node.number:
        node.right = insert(node.right, number)

    return node


def search(node, number):
    if node is None:
        return False

    if node.number == number:
        return True

    if number < node.number:
        return search(node.left, number)
    else:
        return search(node.right, number)


def inorder(node):
    # Left side, then the node, then the right side
    if node is not None:
        inorder(node.left)
        print(node.number, end=" ")