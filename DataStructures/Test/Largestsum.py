arr = [12, -2, -3, 4, -1, 1, 5, -3, 4]

from sys import maxsize

n = len(arr)
max_till = -maxsize
max_end = 0
start = end = s = 0

for i in range(0, n):
    max_end += arr[i]
    if max_till < max_end:
        max_till = max_end
        start = s
        end = i

    if max_end < 0:
        max_end = 0
        s = i + 1
print(max_till, start, end)
