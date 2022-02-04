

def BinarySearch(arr,num):

    l = 0
    h = len(arr) -1

    while l <= h:
        mid = (l+h)//2
        if arr[mid] == num:
            print(num,mid)
            break
        elif arr[mid] > num:
            h = mid -1
        else:
            l = mid +1
    else:
        print("NotFound")



arr = [1,2,4,7,9,11,20,35]
num = 20

BinarySearch(arr,353)