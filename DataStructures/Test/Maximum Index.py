def max_index(arr):
    max_num = arr[-1]
    n = len(arr)
    e = n - 1
    s = 0
    diff = 0

    for i in range(n - 2, -1, -1):
        if max_num > arr[i]:
            if e - i > diff:
                diff = e - i
                s = i
        else:
            max_num = arr[i]
            e = i
            s = i
    return diff

arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]
print(max_index(arr))
