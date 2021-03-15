##https://www.geeksforgeeks.org/majority-element/

#my solution using Hashing
arr = [3, 3, 4, 3, 4, 4, 2, 3, 3, 3]
n = len(arr)

mx = n / 2
dic = {}
for i in range(n):
    dic[arr[i]] = 0

for i in range(n):
    dic[arr[i]] += 1
    if dic[arr[i]] > mx:
        print(arr[i])


##using sort and compare ajecnt element
arr = [3, 3, 4, 3, 4,1, 4, 2, 3, 3, 3]
n = len(arr)

maj = n / 2
arr.sort()
max = arr[0]
count = 1
for i in range(n-1):
    if arr[i] == arr[i +1]:
        max = arr[i]
        count +=1
        if count > maj:
            print(arr[i])
    else:
        max = arr[i]
        count = 1
