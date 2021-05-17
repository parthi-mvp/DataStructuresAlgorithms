# https://www.geeksforgeeks.org/next-greater-element/

def nextLargerElement(arr, n):
    stack = []
    arr1 = [0 for i in arr]

    for i in range(n - 1, -1, -1):
        while len(stack) != 0 and stack[-1] <= arr[i]:
            stack.pop()
        if len(stack) == 0:
            arr1[i] = -1
        else:
            arr1[i] = stack[-1]
        stack.append(arr[i])
    for i in range(len(arr)):
        print(arr[i], '-->', arr1[i])
    return arr1


if __name__ == "__main__":
    arr = [6, 8, 0, 1, 3]
    nextLargerElement(arr, len(arr))
