# Problem Description
#
# Given an array A containing N integers.
#
# You need to find the maximum sum of triplet ( Ai + Aj + Ak ) such that 0 <= i < j < k < N and Ai < Aj < Ak.
#
# If no such triplet exist return 0.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)
        ans = 0
        for i in range(1, n - 1):
            max1 = 0
            max2 = 0
            for j in range(0, i):
                if A[j] < A[i]:
                    max1 = max(max1, A[j])
            for j in range(i + 1, n):
                if A[j] > A[i]:
                    max2 = max(max2, A[j])
            if (max1 & max2):
                ans = max(ans, max1 + A[i] + max2)
        return ans


A = [1, 2, 3]
a = Solution()
print(a.solve(A))
