from random import randint

a = [5, 4, 0, 3, 18, 48, 1]

def qsort(arr):
    if len(arr) < 2:
        res = arr
    else:
        l = len(arr)
        rnd = randint(0, l-1)
        mid = (arr[rnd])
        left = [arr[j] for j in range(l) if arr[j] < mid]
        right = [arr[j] for j in range(l) if arr[j] > mid]
        res = qsort(left) + [mid] + qsort(right)
    return res

print(qsort(a))