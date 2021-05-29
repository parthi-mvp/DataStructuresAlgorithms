n = 30

prime = [True for i in range(n + 1)]
prime_num = []
p = 2

while p * p <= n:
    if prime[p] == True:
        for i in range(p * p, n + 1, p):
            print(i)
            prime[i] = False
    p += 1

for p in range(2, n + 1):
    if prime[p]:
        prime_num.append(p)


sum = 16
l = 0
r = len(prime_num) - 1
while l <= r:
    if prime_num[l] + prime_num[r] > sum:
        r -=1
    elif prime_num[l] + prime_num[r] < sum:
        l += 1
    else:
        print(prime_num[l], prime_num[r])
        break
