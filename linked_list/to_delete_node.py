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
            return

        if self.head.data == key:
            self.head = self.head.next
            return

        current = self.head
        while current:
            if current.data == key:
                break
            previous = current
            current = current.next

        if current is None:
            print("Key is found")
        else:
            previous.next = current.next


if __name__ == "__main__":
    linked_list = LinkedList()

    node1 = Node(100)
    linked_list.add_node(node1)

    linked_list.delete_node(node1)

