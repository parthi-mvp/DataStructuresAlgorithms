arr = [1, 2, 3, 2, 1, 4]
print("Using My solution")
arr.sort()
ele = arr[0]
count = 1
# print(len(arr) - 2)
i = 0
while i < len(arr) - 1:
    if arr[i] == arr[i + 1]:
        count += 1
        ele = arr[i]
    else:
        if count % 2 != 0:
            print(ele)
            break
        count = 1
        ele = arr[i + 1]
    if i == len(arr) - 2:
        print(ele)
    i += 1

# using Hashing
print("Using Hashing")
hash = dict()

for i in range(0, len(arr)):
    if arr[i] not in hash:
        hash[arr[i]] = 1
    else:
        hash[arr[i]] += 1

for k in hash:
    if hash[k] % 2 != 0:
        print(k)
        break

# Using XOR
print("Using XOR")


# Test array
arr = [1, 2, 3, 2, 3, 1, 4]
res = 0
for element in arr:
    res = res ^ element

print(res)




