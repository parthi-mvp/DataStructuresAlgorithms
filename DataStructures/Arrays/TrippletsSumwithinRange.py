def solve(A):
    A.sort()
    n = len(A)
    low = 7
    up = 11
    lis = []
    for i in range(1, n - 2):
        j = i + 1
        k = n - 1
        while j < k:
            cur_sum = A[i] + A[j] + A[k]
            if low < cur_sum and up> cur_sum:
                lis.append(cur_sum)
                j = j + 1
                k = k - 1
            elif low > cur_sum:
                j = j + 1
            else:
                k = k - 1

    return lis

print(solve([8, 3, 5, 2]))
