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
        print(current.data)

    def delete_node(self, key):
        if self.head is None:
            print("The list is empty")


if __name__ == "__main__":
    linked_list = LinkedList()

