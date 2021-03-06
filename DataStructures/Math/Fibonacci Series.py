def fib(n):
    F = [[1, 1],
         [1, 0]]

    M = [[1, 1],
         [1, 0]]

    for i in range(2, n ):
        x = (F[0][0] * M[0][0]) + (F[0][1] * M[1][0])
        y = (F[0][0] * M[0][1]) + (F[0][1] * M[1][1])
        z = (F[1][0] * M[0][0]) + (F[1][1] * M[1][0])
        w = (F[1][0] * M[0][1]) + (F[1][1] * M[1][1])

        F[0][0] = x
        F[0][1] = y
        F[1][0] = z
        F[1][1] = w

    return F[0][0]%(10**9+7)


print(fib(10001))
