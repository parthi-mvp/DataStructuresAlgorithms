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




