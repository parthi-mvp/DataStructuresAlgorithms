class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n:
                print(n.data, '-->', end=' ')
                n = n.next
            print(n)

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = node

    def insert_after_item(self, x, data):
        n = self.head
        print(n.next)
        while n is not None:
            if x == n.data:
                break
            n = n.next
        if n is None:
            print("Item not found")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def insert_before_item(self, x, data):
        n = self.head
        new_node = Node(data)
        if n is not None:
            if x == n.data:
                n = new_node
                n.next = None
                return
        while n is not None:
            if x == n.data:
                break
            p = n
            n = n.next
        if n is None:
            print("Item not found")
        else:
            p.next = new_node
            new_node.next = n

    def deleteNode(self, data):
        n = self.head
        if n is not None:
            if data == n.data:
                self.head = n.next
                n = None
                return
        while n:
            if data == n.data:
                break
            p = n
            n = n.next
        if n is None:
            print("Item not found in Linked list")
        else:
            p.next = n.next
            n = None

    def deleteAtPos(self, pos):
        n = p = self.head
        if n is not None:
            if pos == 0:
                self.head = n.next
                n = None
                return
        i = 0
        while n:
            if i == pos:
                p.next = n.next
                n = None
                return
            p = n
            n = n.next
            i += 1

    def reverse(self, head):
        pre = nex = None
        cur = head

        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        self.head = pre

    def reverrec(self, head):

        if head is None or head.next is None:
            return head

        # Reverse the rest list
        rest = self.reverrec(head.next)

        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the header pointer
        return rest

    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +
                             str(temp.data) + " --> ")
            temp = temp.next
        return linkedListStr

# # Driver code
# linkedList = LinkedList()
# linkedList.push(20)
# linkedList.push(4)
# linkedList.push(15)
# linkedList.push(85)
#
# print("Given linked list")
# print(linkedList)
#
# linkedList.reverrec(linkedList.head)
#
# print("Reversed linked list")
# print(linkedList)
