from LinkedListC import LinkedList


def findMid(head):
    c = 0
    mid = head
    ll = head
    while ll is not None:
        if c % 2 != 0:
            mid = mid.next
        c += 1
        ll = ll.next
    return (mid.data)


def sol2(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data


def createlist(arr):
    ll = LinkedList()
    for i in arr:
        ll.append(i)
    ll.print()
    return ll.head


if '__main__' == __name__:
    arr = [1, 10, 23, 12, 23, 34]
    list = createlist(arr)
    print(findMid(list.head))
    print(sol2(list.head))
