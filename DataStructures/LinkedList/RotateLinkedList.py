from LinkedListC import LinkedList

def RotateList(head, k):
    first = head
    h_node = head
    i = 1
    while head.next:
        next = head.next
        if i == k:
            head.next = None
            h_node = next
        head = next
        i += 1
    if k == i:
        return first
    head.next = first
    return h_node


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 4, 5, 6, 7]
    ll = LinkedList()
    for i in arr:
        ll.append(i)

    print(ll)
    ll.head = RotateList(ll.head, 8)
    print(ll)
