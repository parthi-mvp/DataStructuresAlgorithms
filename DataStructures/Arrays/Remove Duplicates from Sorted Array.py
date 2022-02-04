def remove_dup(A):
    j =0
    n=len(A)
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            A[j] = A[i]
            j += 1
    A[j] = A[n-1]
    print(A)
    return j



A = [1, 2, 2, 3, 4, 4, 4]

print(remove_dup(A))