# https://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/

print("My Solution")
arr1 = [1, 3, 3, 4, 5, 7]
arr2 = [2, 3, 3, 4, 4, 5]

l_a1 = len(arr1)
l_a2 = len(arr2)

union = []
ins = []
i = 0
j = 0

while i < l_a1 and j < l_a2:
    if arr1[i] < arr2[j]:
        union.append(arr1[i])
        i += 1
    elif arr1[i] == arr2[j]:
        union.append(arr1[i])
        ins.append(arr1[i])
        i += 1
        j += 1
    else:
        union.append(arr2[j])
        j += 1

# while can be used as well
if i == l_a1:
    for a in range(j, l_a2):
        union.append(arr2[a])
if j == l_a2:
    for a in range(i, l_a1):
        union.append(arr1[a])

print(union, ins)

print("Greeks Solution with duplicates in array")

arr1 = [1, 3, 3, 4, 5, 7]
arr2 = [2, 3, 3, 4, 4, 5]

l_a1 = len(arr1)
l_a2 = len(arr2)

union = []
ins = []

if arr1[0] <= arr2[0]:
    union.append(arr1[0])
    i = 1
    j = 0
else:
    union.append(arr2[0])
    j = 1
    i = 0

while i < l_a1 and j < l_a2:
    if arr1[i] < arr2[j]:
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    elif arr1[i] == arr2[j]:
        if len(ins) > 0 and ins[-1] == arr1[i]:
            i += 1
            j += 1
        else:
            if union[-1] != arr1[i]:
                union.append(arr1[i])

            ins.append(arr1[i])
            i += 1
            j += 1
    else:
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

# while can be used as well
if i == l_a1:
    for a in range(j, l_a2):
        union.append(arr2[a])
if j == l_a2:
    for a in range(i, l_a1):
        union.append(arr1[a])

print(union, ins)
