#https://www.geeksforgeeks.org/function-to-check-if-a-singly-linked-list-is-palindrome/

from LinkedListC import LinkedList

def reverse(head):
    curr = head
    per = next = None

    while curr:
        next = curr.next
        curr.next = per
        per = curr
        curr = next

    return per


def comapre(first, second):
    while first:
        if first.data == second.data :
            first = first.next
            second = second.next
        else:
            return False
    return True


def ParthisAlgo(head):
    stk = []
    temp = head
    while temp:
        stk.append(temp.data)
        temp = temp.next

    while head:
        if head.data == stk.pop():
            head = head.next
        else:
            return False
    return True


def Palindrome(head):

    slow_ptr = fast_ptr = head
    prev_slow_ptr = None
    mid = None

    while fast_ptr != None and fast_ptr.next != None:
        fast_ptr = fast_ptr.next.next
        prev_slow_ptr = slow_ptr
        slow_ptr = slow_ptr.next

    if fast_ptr != None:
            mid = slow_ptr
            slow_ptr = slow_ptr.next

    second_half = slow_ptr

    prev_slow_ptr.next = None

    second_half = reverse(second_half)
    print(second_half)
    res = comapre(head,second_half)

    if(mid != None):
        prev_slow_ptr.next = mid
        mid.next = reverse(second_half)
    else:
        prev_slow_ptr.next = reverse(second_half)
    return res


if '__main__' == __name__:
    ll = LinkedList()
    ll.append('q')
    ll.append('2')
    ll.append('2')
    ll.append('q')

    print(ll)
    res = Palindrome(ll.head)
    print(f"Palaindrom - {res}")

