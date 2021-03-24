# https://www.geeksforgeeks.org/replace-every-element-with-the-greatest-on-right-side/


arr = [16, 17, 4, 13, 5, 2]
n = len(arr)
max = arr[n - 1]
arr[n - 1] = -1

for i in range(n - 2, -1, -1):
    temp = arr[i]
    arr[i] = max

    if max < temp:
        max = temp

print(arr)