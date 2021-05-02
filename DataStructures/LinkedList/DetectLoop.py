class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.flag = False


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


def detectLoop(head):
    temp = head
    while temp:
        if temp.flag:
            return True
        temp.flag = True
        temp = temp.next
    return False


if __name__ == '__main__':
    arr = [1, 2, 3, 4]

    ll = LinkedList()
    for i in arr:
        ll.append(i)
    ll.head.next.next.next = ll.head
    loop = detectLoop(ll.head)
    if loop:
        print("Loop detected")
    else:
        print("Loop Not detected")
