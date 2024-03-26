class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(0)

    def add_node(self, node:Node):
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = node

    def add_to_beginning(self, node:Node):
        node.next = self.head.next
        self.head.next = node

    def print_linked_list(self):
        current = self.head
        while current is not None:
            print (current.data)
            current = current.next

    def print_size(self):
        current = self.head

