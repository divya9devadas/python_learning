class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(0)

    def add_node(self, node: Node):
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = node

    def add_to_beginning(self, node: Node):
        node.next = self.head.next
        self.head.next = node

    def print_linked_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def print_size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
            return count - 1


if __name__ == "__main__":
    for number in [25, 50, 100, 150, 200, 250, 300]:
        node = Node(number)
        linked_list = LinkedList()
        linked_list.add_node(node)

    linked_list.print_linked_list()
    print(linked_list.print_size)
