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

    def search(self, target_node: Node):
        current = self.head
        while current is not None:
            if current.data == target_node.data:
                print("Element found")
                return
            current = current.next
        print("Element not found")
        return


if __name__ == "__main__":
    linked_list = LinkedList()
    nodes = [Node(num) for num in [25, 50, 100, 150, 200, 250, 300]]
    for node in nodes:
        linked_list.add_node(node)

    target_node = Node(10)
    linked_list.search(target_node)
