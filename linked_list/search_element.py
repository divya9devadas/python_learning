class LinkedList:
    def __init__(self):
        self.head = Node(0)

    def add_node(self, node: Node):
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = node

def search(self, target_node:Node):
    current = self.head
    while current is not None
        if current.data == target_node.data:
            print("Found")
            return
        current = current.next
    print("Not found")
    return

if __name__ == "__main__":
    target_node = Node(50)

