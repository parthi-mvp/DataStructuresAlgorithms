from LinkedListC import LinkedList


def SwapNodes(head_ref, x, y):
    head = head_ref

    if (x == y):
        return None

    currX = None
    currY = None
    perX = perY = per = None

    while head_ref:
        if (head_ref.data == x):
            currX = head_ref
            perX = per
        elif (head_ref.data == y):
            currY = head_ref
            perY = per
        per = head_ref
        head_ref = ((head_ref).next)

    if currY != None and currY != None:
        if perX == None:
            head = currY
        else:
            perX.next = currY

        if perY == None:
            head = currX
        else:
            perY.next = currX
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    return head


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6, 7]
    ll = LinkedList()
    for i in arr:
        ll.append(i)

    print(ll)
    ll.head = SwapNodes(ll.head, 1, 5)
    print(ll)
