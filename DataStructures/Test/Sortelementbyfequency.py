# 45 mins

a = [2, 5, 2, 8, 5, 6, 8, 8, 6, 6]
n = len(a)
pos_arr = []
for i in range(0, n):
    pos_arr.append([a[i], i])
print(pos_arr)
pos_arr.sort()
print(pos_arr)
arr = []
count = 1
num = pos_arr[0]
for i in range(1, n):
    if pos_arr[i][0] == num[0]:
        count += 1
    else:
        num.append(count)
        arr.append(num)
        num = pos_arr[i]
        count = 1
    if i == n - 1:
        num.append(count)
        arr.append(num)

print(arr)


def mergesort(arr, l, pos):
    if l > 1:
        mid = l // 2
        left = arr[:mid]
        right = arr[mid:]
        l_left = len(left)
        l_right = len(right)
        mergesort(left, l_left, pos)
        mergesort(right, l_right, pos)

        i = j = k = 0
        while i < l_left and j < l_right:
            if left[i][pos] > right[j][pos]:

                arr[k] = left[i]
                i += 1
                k += 1
            elif left[i][pos] == right[j][pos]:
                if left[i][1] < right[j][1]:
                    arr[k] = left[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = right[j]
                    j += 1
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


mergesort(arr, len(arr), 2)
print(arr)
for i in arr:
    print(f'{str(i[0]) * i[2]}', end='')
