# https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

arr = [4, 2, 4, 5, 2, 3, 1]
n = 5

arr.sort()
for i in range(1, len(arr)):
    if arr[i - 1] == arr[i]:
        print(arr[i])

print("maths formula a-b whole square")
S = arr[0]
P = arr[0]
for i in arr:
    S = S + i
    P = P * i


