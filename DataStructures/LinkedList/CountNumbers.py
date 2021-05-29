class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.count = 0

    def print(self):
        n = self.head
        while n:
            print(n.data, "-->", end="")
            n = n.next
        print("None")

    def append(self, data):
        n = self.head
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        while n.next is not None:
            n = n.next
        n.next = node

    def count1(self, a):
        n = self.head
        count = 0
        while n is not None:
            if n.data == a:
                count += 1
            n = n.next

    ##with recursion
    def count_rec(self, li, a):
        if not li:
            print(self.count)
            return self.count

        if li.data == a:
            self.count = self.count + 1
        print(li.data)
        return self.count_rec(li.next, a)


llist = LinkedList()
llist.append(1)
llist.append(3)
llist.append(1)
llist.append(2)
llist.append(1)

llist.print()
# print(llist.count1(1))
print(llist.count_rec(llist.head, 1))
