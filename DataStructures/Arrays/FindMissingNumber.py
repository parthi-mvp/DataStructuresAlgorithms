# https://www.geeksforgeeks.org/find-the-missing-number/

print('My solution #1')

a = [2, 3, 6, 5, 7, 4]
n = len(a)
a.sort()
c = 1
for i in a:
    if i != c:
        print(c)
        break
    c += 1

print("My solution #2")


def findmissing(arr, s, e):
    for i in range(s, e):
        if arr[i - 1] != i:
            print(c)
            break


mid = n // 2
if a[mid] != mid + 1 and a[mid - 1] == mid and a[mid] == mid + 2:
    print(mid + 1)
elif a[mid] != mid + 1:

    findmissing(a[:mid], 1, mid + 1)
else:

    findmissing(a[mid:], mid, n)

print('using Summation')

size = len(a)
n = size + 1
sum = n * (n + 1) / 2
arr_sum = 0
for i in a:
    arr_sum += i

print(int(sum - arr_sum))

print('Using XOR')

a = [1, 2, 4, 3, 6]
n = len(a)
x1 = 0
x2 = 1
for i in a:
    x1 = x1 ^ i
for i in range(2, n + 2):
    x2 = x2 ^ i
print(x1 ^ x2)
