from LinkedListC import LinkedList


def solve(s):
    A = s
    count = 0
    while A:
        if A.data == 0:
            count += 1
        A = A.next
    i = 0
    val = 0
    A = s
    while A:
        if i >= count:
            val = 1
        A.data = val
        i += 1
        A= A.next
    return s

ll = LinkedList()
ll.push(0)
ll.push(1)
ll.push(1)
ll.push(0)
ll.print()


a = solve(ll.head)
print(a.print())