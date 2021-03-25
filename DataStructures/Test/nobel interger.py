# You are given a read only array of n integers from 1 to n.
#
# Each integer appears exactly once except A which appears twice and B which is missing.
#
# Return A and B.
#
# Input:[3 1 2 5 3]
#
# Output:[3, 4]
#
# A = 3, B = 4


#20 mins

arr = [1,1,3,3]

arr.sort()
n = len(arr)


def nobel_number(arr, n):
    c = 0
    for i in range(n-1, -1, -1):
        if arr[i] == c:
            print('nobe integer ',arr[i] )
            return 1
        c += 1
    return -1


print(nobel_number(arr,n))
