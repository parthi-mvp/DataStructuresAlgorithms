# https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

arr = [50,50,70]

n = len(arr)

if arr[0] >= arr[1]:
    print(arr[0])

if arr[n - 1] > arr[n - 2]:
    print(arr[n - 1])

for i in range(1, n - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        print(arr[i])
