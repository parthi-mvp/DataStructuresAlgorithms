class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def append(self,data):
        new = Node(data)
        n = self.head
        while n.next:
            n = n.next
        n.next = new

    def print(self):
        n = self.head
        while n:
            print(n.data ,end=' ')
            n= n.next






ll = LinkedList()
ll.push(1)
ll.push(2)
ll.append(3)
ll.print()
