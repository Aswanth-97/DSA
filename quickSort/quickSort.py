def quickSort(L, l, r):
    if r - l <= 1:
        return L
    pivot = L[l]
    lower = l + 1
    higher = l + 1
    for i in range(l + 1, r):
        if L[i] > pivot:
            higher += 1
        else:
            L[i], L[lower] = L[lower], L[i]
            lower += 1
            higher += 1
    L[l], L[lower - 1] = L[lower - 1], L[l]
    quickSort(L, l, lower-1)
    quickSort(L, lower, higher)
    return L


L = [9, 4, 2, 6, 8, 10, 4, 15, 16, 20, 1, 7, 5]

print(quickSort(L, 0, len(L)))
