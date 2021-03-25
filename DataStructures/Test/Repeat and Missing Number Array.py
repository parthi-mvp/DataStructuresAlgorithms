# Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.
# Output Format:
# Return 1 if any such integer p is found else return -1.
# A = [3, 2, 1, 3] , Output = 1
# A = [1, 1, 3, 3] , Output = -1

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
