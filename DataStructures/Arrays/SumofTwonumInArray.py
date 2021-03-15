# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

a = [0, -1, 2, -3, 1]
s = len(a)
sum = -2
a.sort()
l = 0
r = s - 1
while l < r:
    if a[l] + a[r] < sum:
        l += 1
    elif a[l] + a[r] == sum:
        print(a[l], a[r])
        l += 1
    else:
        r += -1

# using hash table
ht = set()

for i in range(s):
    temp = sum - a[i]
    if temp in ht:
        print(temp, a[i])
    ht.add(a[i])
