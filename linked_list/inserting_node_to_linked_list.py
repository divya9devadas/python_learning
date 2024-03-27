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


if __name__ == "__main__":
    linked_list = LinkedList()

    node1 = Node(100)
    linked_list.add_node(node1)

    node2 = Node(200)
    linked_list.add_node(node2)

    node3 = Node(300)
    linked_list.add_node(node3)

    node4 = Node(400)
    linked_list.add_node(node4)

    node5 = Node(500)
    linked_list.add_node(node5)
