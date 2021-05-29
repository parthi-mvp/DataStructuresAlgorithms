# 30mins

# Given an array of integers A of size N and an integer B.
#
# array A is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
#
# You are given a target value B to search. If found in the array, return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# NOTE:- Array A was sorted in non-decreasing order before rotation


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def binary_search(self, arr, e):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == e:
                return mid
            elif arr[mid] < e:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def search(self, A, B):
        r = -1
        n = len(A)
        if A[0] < A[-1]:
            return self.binary_search(A, B)
        for i in range(n - 1, -1, -1):
            if A[i] < A[i - 1]:
                r = i
        if B >= A[0]:
            print(A[0:r])
            ans = self.binary_search(A[0:r], B)
        else:
            print(A[r:n])
            ans = self.binary_search(A[r:n], B)
            if ans != -1:
                return ans + r
        return ans


# A = [4, 5, 6, 7, 1, 2, 3]
# B = 8
# a = Solution()
# print(a.search(A, B))
#

# better solution

def binary_search(arr, e):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == e:
                return mid
            elif arr[mid] <= arr[r]:
                if arr[mid] < e <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if arr[mid] > e >= arr[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


A = [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
B = 202
print(binary_search(A, B))
