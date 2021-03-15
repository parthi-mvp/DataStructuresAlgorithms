# My Answer
arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
l = len(arr)


def reverse(arr, s, d):
    i = s
    j = d - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    # print(arr)


reverse(arr, 0, d)
reverse(arr, d, l)
reverse(arr, 0, l)
print(arr)

# METHOD 1 (Using temp array)
