#time 40 mins


class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        a_len = len(A)
        b_len = len(B)
        full_len = a_len + b_len
        new = []
        med = full_len // 2
        i = j = 0
        while i < a_len and j < b_len:
            if len(new) == med + 2:
                break
            if A[i] < B[j]:
                new.append(A[i])
                i += 1
            elif B[j] < A[i]:
                new.append(B[j])
                j += 1
            else:
                new.append(A[i])
                new.append(A[i])
                i += 1
                j += 1

        while i < a_len:
            if len(new) == med + 1:
                break
            new.append(A[i])
            i += 1

        while j < b_len:
            if len(new) == med + 1:
                break
            new.append(B[j])
            j += 1
        print(new,med,full_len)
        if full_len % 2 != 0:
            return float(new[med])
        else:
            return float((new[med - 1] + new[med]) / 2)


A =[ -37, -9, 10, 19 ]
B = [ -29, 18 ,35,40]
a = Solution()
print(a.findMedianSortedArrays(A,B))