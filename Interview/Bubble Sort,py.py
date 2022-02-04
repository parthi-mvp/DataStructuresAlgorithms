arr = [25,1,14,2,8,3]
l = len(arr)
i=0
j=1
swapped = False

while True:
    if arr[i] > arr[j]:
        arr[i] ,arr[j] = arr[j] ,arr[i]
        swapped = True

    if j == l -1:
        i = 0
        j = 1
        if swapped is False:
            break
        else:
            swapped = False
        continue

    i += 1
    j += 1

print(arr)