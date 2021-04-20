class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n:
                print(n.data, '-->', end=' ')
                n = n.ref

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        n = self.head
        while n.ref is not None:
            n = n.ref
        n.ref = node

    def insert_after_item(self, x, data):
        n = self.head
        print(n.ref)
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Item not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def insert_before_item(self, x, data):
        n = self.head
        new_node = Node(data)
        if n is not None:
            if x == n.data:
                n = new_node
                n.ref = None
                return
        while n is not None:
            if x == n.data:
                break
            p = n
            n = n.ref
        if n is None:
            print("Item not found")
        else:
            p.ref = new_node
            new_node.ref = n


    def deleteNode(self, data):
        n = self.head
        if n is not None:
            if data == n.data:
                self.head = n.ref
                n = None
                return
        while n:
            if data == n.data:
                break
            p=n
            n = n.ref
        if n is None:
            print("Item not found in Linked list")
        else:
            p.ref = n.ref
            n = None

    def deleteAtPos(self,pos):
        n = p = self.head
        if n is not None:
            if pos == 0:
                self.head = n.ref
                n = None
                return
        i=0
        while n:
            if i == pos:
                p.ref = n.ref
                n=None
                return
            p=n
            n = n.ref
            i +=1

ll = LinkedList()

ll.insert_at_start(11)
ll.insert_at_start(13)
ll.insert_at_start(14)

ll.traverse()
# ll.insert_at_end(13)
# ll.insert_at_start(11)
# ll.insert_at_start(9)
# ll.insert_after_item(9, 10)
# ll.insert_before_item(13, 100)
ll.deleteAtPos(0)
print()

ll.traverse()
