a = [-2, -3, -6, -2, -3,0]

max_so_far = a[0]
curr_max = a[0]

for i in range(1, len(a)):
    curr_max = max(a[i], curr_max + a[i])
    max_so_far = max(max_so_far, curr_max)

print(max_so_far)


from sys import maxsize
max_ending_here = 0
max_so_far = -maxsize
start = 0
end = 0
s=0

for i in range(0,len(a)):
    max_ending_here += a[i]
    if max_ending_here > max_so_far:
        max_so_far = max_ending_here
        start = s
        end = i

    if max_ending_here < 0:
        max_ending_here = 0
        s = i+1


print(max_so_far,start,end)
