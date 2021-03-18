arr = [0, 1, 2, 0, 1, 2]

print("My solution - using mege sort :)")

print("Using count or hash")

c0 = c1 = c2 = 0

for i in range(0, len(arr)):
    if arr[i] == 0:
        c0 += 1
    if arr[i] == 1:
        c1 += 1
    if arr[i] == 2:
        c2 += 1

print(str(0) * c0, str(1) * c1, str(2) * c2)

print("Dutch National Flag Algorithm OR 3-way Partitioning")

low = mid = 0
high = len(arr) - 1
arr = [0, 1, 2, 0, 1, 2]
while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        low += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1

print(arr)
