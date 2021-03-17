# https://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/

arr = [1, 60, -10, 70, -80, 85, 2]
size = len(arr)
arr.sort()
l = 0
r = size - 1
el1 = arr[l]
el2 = arr[r]
min_sum = arr[l] + arr[r]

while l < r:
    sum = arr[l] + arr[r]
    if abs(sum) < abs(min_sum):
        min_sum = sum
        el1 = arr[l]
        el2 = arr[r]
    if sum < 0:
        l += 1
    else:
        r -= 1

print(el1, el2, 'Sum : ', min_sum)

print("Greek soluton - Wrong one ")
# issue with the sorting - Works if array is sorted

import sys


def findMinSum(arr, n):
    for i in range(1, n):

        # Modified to sort by abolute values
        if (not abs(arr[i - 1]) < abs(arr[i])):
            arr[i - 1], arr[i] = arr[i], arr[i - 1]

    Min = sys.maxsize
    x = 0
    y = 0

    for i in range(1, n):

        # Absolute value shows how
        # close it is to zero
        if (abs(arr[i - 1] + arr[i]) <= Min):
            # If found an even close value
            # update min and store the index
            Min = abs(arr[i - 1] + arr[i])
            x = i - 1
            y = i

    print("The two elements whose sum is minimum are",
          arr[x], "and", arr[y])


# Driver code
arr = [1, 60, -10, 70, -80, 85, 2]

n = len(arr)

findMinSum(arr, n)
