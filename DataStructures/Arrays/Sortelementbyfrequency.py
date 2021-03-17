arr = [2, 5, 2, -1, 6, 9999999, 5, 8, 8, 8]
size = len(arr)


def multidim_mergesort(arr, pos):
    if len(arr) > 1:
        mid = len(arr) // 2  # get middle element
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        multidim_mergesort(left_arr, pos)
        multidim_mergesort(right_arr, pos)

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i][pos] > right_arr[j][pos]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]

            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]

            j += 1
            k += 1


# sort to compare index if elemetes are same.
def sortCompareindex(arr, pos):
    if len(arr) > 1:
        mid = len(arr) // 2  # get middle element
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        multidim_mergesort(left_arr, pos)
        multidim_mergesort(right_arr, pos)

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i][pos] > right_arr[j][pos]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            elif left_arr[i][pos] == right_arr[j][pos]:
                if left_arr[i][1] < right_arr[j][1]:
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1

            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]

            j += 1
            k += 1


ar = []
# get 2D array by position
for i in range(0, size):
    ar.append([arr[i], i + 1])

multidim_mergesort(ar, 0)
print(ar)
count = 1
new = []
min = ar[0]
for i in range(1, size):
    if ar[i - 1][0] == ar[i][0]:
        count += 1
        if ar[i][1] < min[1]:
            min = ar[i]
    else:
        min.append(count)
        new.append(min)
        count = 1
        min = ar[i]
    if i == size - 1:
        min.append(count)
        new.append(min)
print(new)
sortCompareindex(new, 2)
print(new)
print("Result")
for i in range(0, len(new)):
    print(str(new[i][0]) * new[i][2], end=" ")
