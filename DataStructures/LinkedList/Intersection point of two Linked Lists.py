# https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/

from LinkedListC import LinkedList


# navie approach
def insertion_point(ll1, ll2):
    first = ll1.head
    second = ll2.head
    while first:
        second = ll2.head
        while second:
            if first == second:
                return first
            second = second.next
        first = first.next


def insertion_using_count(ll1, ll2, diff):
    first = ll1.head
    second = ll2.head
    i = 0
    while first:
        if i == diff:
            break
        i += 1
        first = first.next
    while first:
        if first == second:
            return first.data
        first = first.next
        second = second.next


if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append('1')
    ll1.append('2')
    ll1.append('41')
    ll1.append('52')
    ll1.append('20')
    ll1.append('31')
    ll1.append('41')

    ll2.append('4')
    ll2.append('3')
    ll2.append('5')
    ll2.append('6')

    ll1.print()

    ins = ll1.head.next.next.next.next
    ll2.head.next.next = ins
    ll2.print()
    len_1 = ll1.length()
    len_2 = ll2.length()
    diff = len_1 - len_2
    if diff > 0:
        print(insertion_using_count(ll1, ll2, abs(diff)))
    else:
        print(insertion_using_count(ll2, ll1, abs(diff)))
    print()
