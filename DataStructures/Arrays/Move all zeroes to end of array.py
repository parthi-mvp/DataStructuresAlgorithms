# https://www.geeksforgeeks.org/move-zeroes-end-array/

arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]

n = len(arr)
i = j = 0

while i < n and j < n:
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j += 1
    else:
        i += 1

print(arr)

print("Greeks solution")
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
c = 0

for i in range(0, n):
    if arr[i] != 0:
        arr[c] = arr[i]
        c += 1

while c < n:
    arr[c] = 0
    c += 1

print(arr)
