def find_max(arr):
    incl = 0
    excl = 0

    for i in arr:
        new_excl = max(excl, incl)
        incl = excl + i
        excl = new_excl

    return max(incl, excl)


arr = [5, 5, 10, 100, 10, 5]
print(find_max(arr))
