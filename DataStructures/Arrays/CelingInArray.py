print("my Solution #1")

arr = [1, 2, 8, 10, 10, 12, 19]
n = len(arr)
x = 1

for i in range(0, n):
    if arr[i] > x:
        if i == 0:
            print(f'No celing')
            print(f'Floor - {arr[i]}')
        else:
            print(f'Celing - {arr[i]}')
            print(f'Floor - {arr[i - 1]}')
        break
    if i == n - 1 and arr[i] <= x:
        print(f'No Floor')
        print(f'Celeing - {arr[i]}')

print("Binary Search solution")
arr = [1, 2, 8, 10, 10, 12, 19]
l = 1
r = n - 2
x = 5
if arr[0] < x:
    print(f'No celing')
    print(f'Floor - {arr[l]}')

if arr[n-1] > x:
    print(f'No Floor')
    print(f'Celeing - {arr[r]}')

while l < r:
    mid = l + (l-r)//2

    if arr[mid] == x:
        print(f'celeing - {arr[mid]}')
        print(f'Floor - {arr[mid]}')
        break
    if arr[mid]< x :
        r = mid -1
    else:
        l = mid + 1





