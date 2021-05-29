A = [1 ]

n = len(A)
A.sort()
print(A)
a = 1
for i in range(0, len(A)):
    if A[i] > 0:
        if A[i] == a:
            a = A[i] + 1
        else:
            print(a)
            break
print(a)

