class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def singly_linked_list(a, b, c, d, e):
    node1 = Node(a)
    node2 = Node(b)
    node3 = Node(c)
    node4 = Node(d)
    node5 = Node(e)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    current_node = node1
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")


def doubly_linked_list(a, b, c, d, e):
    node1 = Node(a)
    node2 = Node(b)
    node3 = Node(c)
    node4 = Node(d)
    node5 = Node(e)
    node1.next = node2
    node2.next = node3
    node2.prev = node1
    node3.next = node4
    node3.prev = node2
    node4.next = node5
    node4.prev = node3
    node5.prev = node4

    print("Forward")
    current_node = node1
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")

    print("Backward")
    current_node = node1
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.prev
    print("null")


def circular_linked_list(a, b, c, d, e):
    node1 = Node(a)
    node2 = Node(b)
    node3 = Node(c)
    node4 = Node(d)
    node5 = Node(e)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    current_node = node1
    start_node = node1
    print(current_node.data, end=" -> ")
    current_node = current_node.next

    while current_node != start_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("...")


def find_lowest_value_linked_list(head):
    min_value = head.data
    current_node = head.next
    while current_node:
        if current_node.data < min_value:
            min_value = current_node.data
        current_node = current_node.next
    return min_value


def traverse(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")


def delete_node(head, node):
    if head == node:
        return head.next

    current_node = head
    while current_node.next and current_node.next != node:
        current_node = current_node.next

    if current_node.next is None:
        return head

    current_node.next = current_node.next.next

    return head


def insert_node(head, node, position):
    if position == 1:
        node.next = head
        return node

    current_node = head
    for i in range(1, position - 1):
        if current_node is None:
            break
        current_node = current_node.next

    node.next = current_node.next
    current_node.next = node
    return head


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

new_node = Node(10)

node1 = insert_node(node1, new_node, 6)

print("\nAfter insertion:")
traverse(node1)
