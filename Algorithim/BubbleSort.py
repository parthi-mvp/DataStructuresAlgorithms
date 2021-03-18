arr = [1, 4, 2, 6, 3,2]

l = 1
while l > 0:
    l=0
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
            l=1
print(arr)

