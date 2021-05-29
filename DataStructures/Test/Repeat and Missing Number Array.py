

# Time taken 13 mins

arr = [3, 1, 2, 5, 3]

n = len(arr)

new = [0] * n
repeat = 0
miss = 0
for i in range(0, n):
    if arr[i] - 1 == 1:
        repeat = arr[i] + 1
        break
    new[arr[i] - 1] += 1

sum = int(n * (n + 1) / 2)
arr_sum = arr[0] - repeat
for i in range(1, n):
    arr_sum += arr[i]

miss = sum - arr_sum

print(f'A = {repeat} , B = {miss}')
