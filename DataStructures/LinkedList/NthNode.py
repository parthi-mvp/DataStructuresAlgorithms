class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def print(self):
        n = self.head
        while n:
            print(n.data, "-->", end="")
            n = n.next

    def append(self, data):
        n = self.head
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        while n.next is not None:
            n = n.next
        n.next = node

    def findNthNode(self, x):
        n = self.head
        i = 0
        while n is not None:
            if i == x:
                print(n.data)
                return
            i += 1
            n = n.next
        print("Index out of Range")


ll = LinkedList()
for i in range(10):
    ll.append(i)

ll.findNthNode(0)

ll.print()
