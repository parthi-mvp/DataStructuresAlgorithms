# https://www.geeksforgeeks.org/find-the-missing-number/

print('My solution ')

a = [1, 2, 4,3,6]
a.sort()
c = 1
for i in a:
    if i != c:
        print(c)
        break
    c += 1


print('Summation')

size = len(a)
n = size + 1
sum = n*(n+1)/2
arr_sum = 0
for i in a:
    arr_sum += i

print(int(sum - arr_sum))