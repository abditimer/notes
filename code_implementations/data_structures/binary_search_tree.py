# BST: left_subtree(keys) <= node(key) <= right_subtree(keys)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data=data

def binary_insert(tree, node):
    if tree is None:
        tree = node
    else:
        # if new value is less than the tree value
        if tree.data > node.data:
            if tree.left is None:
                tree.left = node
            else:
                binary_insert(tree.left, node)
        else:
            if tree.right is None:
                tree.right = node
            else:
                binary_insert(tree.right, node)

def binary_search(tree, value):
    # check the left subtree
    if value < tree.data:
        if tree.left is None:
            print(f'{value} not found')
        return binary_search(tree.left, value)
    # check the right subtree
    elif value > tree.data:
        if tree.right is None:
            print(f'{value} not found')
        return binary_search(tree.right, value)
    else:
        print(f'tree has the value {tree.data}, which is equal to {value}, our search value.')

def better_binary_search(tree, value):
    if tree is None:
        print('Not found')
        return Null
    elif tree.data == value:
        print(f'{value} found.')
        return tree
    elif tree.data > value:
        return better_binary_search(tree.left, value)
    else:
        return better_binary_search(tree.right, value)

def in_order_print(tree):
    if not tree:
        return
    in_order_print(tree.left)
    print(tree.data)
    in_order_print(tree.right)

tree = Node(3)
binary_insert(tree, Node(1))
binary_insert(tree, Node(7))
binary_insert(tree, Node(5))

in_order_print(tree)

binary_search(tree, 3)
print('-'*20)
better_binary_search(tree, 3)