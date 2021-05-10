def pickbothsides(arr, n, k):
    windows_sum = sum(arr[:k])
    current_sum = windows_sum
    j = n -1
    for i in range(k-1,-1,-1):
        current_sum = current_sum - arr[i] + arr[j]
        windows_sum = max(windows_sum, current_sum)
        j -= 1
    return windows_sum


if __name__ == "__main__":
    arr = [2, 1, 14, 6, 4, 3]
    n = len(arr)
    k = 3

    print(pickbothsides(arr, n, k))
