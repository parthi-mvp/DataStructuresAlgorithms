def diagonal(A):
    n = len(A)
    res = []
    for a in range(0, n):
        temp = []
        i, j = a, 0
        while i >= 0:
            temp.append(A[j][i])
            j += 1
            i -= 1
        res.append(temp)

    for a in range(1, n):
        temp = []
        i = n - 1
        j = a
        while j <= n - 1:
            temp.append(A[j][i])
            j += 1
            i -= 1
        res.append(temp)
    return res


# interview bit solution
def diagonal1(A):
    n = len(A)
    ans = [[] for i in range(2 * n - 1)]
    for i in range(n):
        for j in range(n):
            ans[i + j].append(A[j][i])
    return ans


if __name__ == "__main__":
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
       ]
    print(diagonal1(A))
