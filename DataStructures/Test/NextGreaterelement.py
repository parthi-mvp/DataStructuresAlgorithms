# https://www.geeksforgeeks.org/next-greater-element/
#45mins
from queue import LifoQueue

A = [11, 13, 21, 3]
s = []
s.append(A[0])
item = next = 0
for i in range(1, len(A), 1):
    cur = A[i]
    if len(s) != 0:
        item = s.pop()
        while item < cur:
            print(item, cur)
            if len(s) == 0:
                break
            item = s.pop()
        if item > cur:
            s.append(item)

    s.append(cur)

while len(s):
    print(s.pop(), -1)
