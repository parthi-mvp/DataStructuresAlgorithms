# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, s):
        A = s
        count = 0
        while A:
            if A.val == 0:
                count += 1
            A = A.next
        i = 0
        val = 0
        A = s
        while A:
            if i >= count:
                val = 1
            A.val = val
            i += 1
            A = A.next
        return s


####### Solution 2
from LinkedListC import LinkedList


def MergeUtil(h1, h2):
    if h1.next is None:
        h1.next = h2
        return h1

    curr1 = h1
    next1 = h1.next
    curr2 = h2
    next2 = h2.next

    while (next1 != None and curr2 != None):
        if curr2.data >= curr1.data and curr2.data <= next1.data:
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1 = curr2
            curr2 = next2

        else:
            if next1.next:
                curr1 = curr1.next
                next1 = next1.next
            else:
                next1.next = curr2
                return h1

    return h1


def MergeLinkedlist(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.data <= l2.data:
        ml = MergeUtil(l1, l2)
    else:
        ml = MergeUtil(l2, l1)
    return ml


if __name__ == "__main__":
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll1.append('1')
    ll1.append('6')
    ll1.append('41')
    ll1.append('52')

    ll2.append('4')
    ll2.append('7')
    ll2.append('10')
    ll2.append('50')
    ll2.append('100')
    a = ll1
    ll1.print()
    ll2.print()

    mll = MergeLinkedlist(ll1.head, ll2.head)
    print("")
