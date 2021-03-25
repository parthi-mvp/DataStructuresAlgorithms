# 10 mins

arr = [-10,3, 6, 1, 2, 7, 2, 3,0]


def mergesoert(arr, l):
    if l > 1:
        mid = l // 2
        left = arr[:mid]
        right = arr[mid:]
        l_left = len(left)
        l_right = len(right)
        mergesoert(left, l_left)
        mergesoert(right, l_right)

        i = j = k = 0

        while i < l_left and j < l_right:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                j += 1
                k += 1

        while i < l_left:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < l_right:
            arr[k] = right[j]
            j += 1
            k += 1


mergesoert(arr, len(arr))
print(arr)
