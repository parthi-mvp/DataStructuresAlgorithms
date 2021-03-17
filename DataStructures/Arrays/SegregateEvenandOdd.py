# https://www.geeksforgeeks.org/segregate-even-and-odd-numbers/

print("My solution 1")
arr = [12, 34, 45, 9, 8, 90, 3, 35]
size = len(arr)

l = 0
for i in range(0, size):
    if arr[i] % 2 == 0:
        temp = arr[l]
        arr[l] = arr[i]
        arr[i] = temp
        l += 1

print(arr)

print("two pointer approach")
l = 0
r = size - 1

while l < r:
    if arr[l] % 2 == 1:
        if arr[r] % 2 == 0:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1
        else:
            r -= 1
    else:
        l += 1
print(arr)
