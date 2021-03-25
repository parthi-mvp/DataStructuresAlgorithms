#https://www.geeksforgeeks.org/next-greater-element/

arr = [4, 5, 2, 25]
n =len(arr)

max = arr[-1]
arr[-1] = -1

for i in range(n-2,-1,-1):
    temp = arr[i]
    arr[i] = max
    if arr[i] > max:
        max = arr[i]

print(arr)