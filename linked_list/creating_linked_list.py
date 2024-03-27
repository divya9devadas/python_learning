class LinkedList:

    def __init__(self, data):
        self.data = data
        self.next = None


node1 = LinkedList(100)
node2 = LinkedList(200)

node1.next = node2
head = node1

current = head
while current is not None:
    print(current.data)
    current = current.next
