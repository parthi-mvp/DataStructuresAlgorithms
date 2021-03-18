print("My solution")
arr = [5, 4, 2, 3, 1, 6]
n = len(arr)

arr.sort()
is_consecutive = True
for i in range(0, n - 2):
    print(arr[i], arr[i + 1])
    if arr[i] != arr[i + 1] - 1:
        is_consecutive = False

print(is_consecutive)

print("Greeks solution ")


def getmax(arr):
    max = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


def getmin(arr):
    min = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


min = getmin(arr)
max = getmax(arr)
is_consecutive = False
if max - min + 1 == n:
    is_consecutive = True
    visted = [False for i in range(n)]
    for i in range(n):
        if visted[arr[i] - min] != False:
            is_consecutive = False
        visted[arr[i] - min] = True

print(is_consecutive)
