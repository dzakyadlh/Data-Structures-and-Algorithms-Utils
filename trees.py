class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order_traversal(node):
    if node is not None:
        print(node.data, end=", ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.data, end=", ")
        in_order_traversal(node.right)


def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=", ")


def left_child_index(index):
    return 2 * index + 1


def right_child_index(index):
    return 2 * index + 2


def pre_order(index, arr):
    if index >= len(arr) or arr[index] is None:
        return []
    return [arr[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index))


def in_order(index, arr):
    if index >= len(arr) or arr[index] is None:
        return []
    return in_order(left_child_index(index)) + [arr[index]] + in_order(right_child_index(index))


def post_order(index, arr):
    if index >= len(arr) or arr[index] is None:
        return []
    return post_order(left_child_index(index), arr) + post_order(right_child_index(index), arr) + [arr[index]]


# O(h)
def search_tree(node, target):
    if node is None:
        return None
    if node.data == target:
        return node
    elif node.data > target:
        return search_tree(node.left, target)
    else:
        return search_tree(node.right, target)


def insert_tree(node, new_node):
    if node is None:
        return TreeNode(new_node)
    if new_node < node.data:
        node.left = insert_tree(node.left, new_node)
    else:
        node.right = insert_tree(node.right, new_node)
    return node


root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG


def smallestString(substrings):
    # Convert each substring to lowercase
    substrings = [substring.lower() for substring in substrings]

    # Sort the substrings using custom comparison rules
    substrings.sort()

    # Concatenate the sorted substrings
    return ''.join(substrings)


# Test
arr = ['a', 'bd', 'ac', 'cd', 'ab']
print(smallestString(arr))
