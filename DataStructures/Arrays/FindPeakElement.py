# https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

arr = [1, 3, 20, 4, 1, 0]

n = len(arr)

if arr[0] >= arr[1]:
    print(arr[0])

if arr[n - 1] > arr[n - 2]:
    print(arr[n - 1])

for i in range(1, n - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        print(arr[i])


# Binary search approach

def findpeak(arr, low, high,n):
    mid = low + (high + low)

    if (mid == 0 or arr[mid-1] <= arr[mid]) and (mid == n-1 or arr[mid+1] <= arr[mid]):
        return mid

    elif mid > 0 and arr[mid-1] > arr[mid]:
        return  findpeak(arr,low,mid-1,n)
    else:
        return findpeak(arr, mid+1, high, n)

print(findpeak(arr,0,n-1,n))