# https://www.geeksforgeeks.org/leaders-in-an-array/
# scan from right
arr = [16, 17, 4, 5, 3, 2]
size = len(arr)

max_ele = arr[size - 1]

for i in range(size - 2, -1, -1):
    if arr[i] > max_ele:
        max_ele = arr[i]
        print(arr[i])
