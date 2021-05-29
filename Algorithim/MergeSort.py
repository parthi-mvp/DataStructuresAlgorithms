def mergesort(arr):  # 38, 27
    if len(arr) > 1:
        mid = len(arr) // 2  # get middle element
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        mergesort(left_arr)
        mergesort(right_arr)

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
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


arr = [123, 27, 143, 3, 159, 82, 110]
mergesort(arr)
print(arr)
