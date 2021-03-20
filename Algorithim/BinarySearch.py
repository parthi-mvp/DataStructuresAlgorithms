# Binary search Algorithm

arr = [10, 20, 80, 30, 60, 50,
       100, 110, 130, 170]
arr.sort()
x = 100

l = 0
r = len(arr) - 1

while l <= r:
    mid = l + (r - l) // 2
    if arr[mid] == x:
        print(mid)
        print(arr[mid])
        break
    elif arr[mid] < x:
        l = mid + 1
    else:
        r = mid - 1
