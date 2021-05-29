from LinkedListC import LinkedList, Node


def printl(ll):
    if ll is None:
        print("Linked List is empty")
    else:
        n = ll
        while n:
            print(n.data, '-->', end=' ')
            n = n.next
        print(n)


def reverse(head):
        curr = head
        per = next = None

        while curr:
            next = curr.next
            curr.next = per
            per = curr
            curr = next
        printl(per)
        return per, head


def k_revrse(head, k):
        curr = h1 = head
        per = None
        next = None
        newhead = None

        i = 1
        while curr:
            next = curr.next
            if i % k == 0:
                curr.next = None
                h, t = reverse(h1)
                if newhead is None:
                    newhead = h
                    per = t
                else:
                    per.next = h
                t.next = next
                per = t
                h1 = next
            curr = next
            i += 1
        return newhead


if __name__ == "__main__":
    ll = LinkedList()
    ll.append('1')
    ll.append('2')
    ll.append('3')
    ll.append('4')
    ll.append('5')
    ll.append('6')
    ll.append('7')
    ll.append('8')

    ll.print()
    a = k_revrse(ll.head, 3)
    printl(a)
