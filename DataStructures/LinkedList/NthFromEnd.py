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

    def findNthfomLast(self, pos):
        main = None
        ref = self.head
        i = 1
        while ref is not None:
            if i >= pos:
                if i == pos:
                    main = self.head
                else:
                    main = main.next
            ref = ref.next
            i += 1
        if main is None:
            print("Index out of range")
        else:
            print(main.data)


ll = LinkedList()
for i in range(5):
    ll.append(i)
ll.findNthfomLast(2)
ll.print()
