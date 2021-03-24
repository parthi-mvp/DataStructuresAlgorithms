ar = [12, 3, 4, 1, 6, 9]
sum = 16
n = len(ar)
ar.sort()


def TripletSum(ar, n, sum):
    for i in range(0, n):
        j = i + 1
        k = n - 1

        while j < k:
            cur_sum = ar[i] + ar[j] + ar[k]
            if cur_sum == sum:
                return (ar[i], ar[j], ar[k])
            elif cur_sum > sum:
                k -= 1
            else:
                j += 1


print(TripletSum(ar, n, sum))

print("Using Hashing")
ar = [12, 3, 4, 1, 6, 9]
sum = 16

for i in range(0, n):
    s = set()
    cur_sum = sum - ar[i]
    for j in range(i + 1, n):
        if (cur_sum - ar[j]) in s:
            print(ar[i], ar[j], cur_sum - ar[j])
        s.add(ar[j])
