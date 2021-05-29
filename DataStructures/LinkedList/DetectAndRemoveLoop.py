class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        n = self.head
        if self.head is None:
            self.head = node
            return
        while n.next is not None:
            n = n.next
        n.next = node

    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +
                             str(temp.data) + " --> ")
            temp = temp.next
        return linkedListStr

    def detectLoop(self):
        slow_p = self.head
        fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                self.removeloop(slow_p)

    def removeloop(self,loop_node):
        ptr1 = self.head


        while(1):
            ptr2 = loop_node
            while ptr2.next != loop_node and ptr2.next != ptr1:
                ptr2 = ptr2.next
            if ptr1 == ptr2.next:
                break
            ptr1 = ptr1.next
        ptr2.next = None




if __name__ == '__main__':
    arr = [1, 2, 3, 4]

    ll = LinkedList()
    for i in arr:
        ll.append(i)
    print(ll)
    ll.head.next.next.next.next = ll.head
    ll.detectLoop()
    print(ll)
