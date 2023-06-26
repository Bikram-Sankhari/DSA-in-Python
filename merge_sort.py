import gc
from random import randint as rand

RANGE = 10
LENGTH = 10


def merge(arr: [], l1: int, h1: int, l2: int, h2: int):
    i = l1
    j = l2
    sorted_array = []

    while i <= h1 and j <= h2:
        if arr[i] <= arr[j]:
            sorted_array.append(arr[i])
            i += 1

        else:
            sorted_array.append(arr[j])
            j += 1

    while i <= h1:
        sorted_array.append(arr[i])
        i += 1

    while j <= h2:
        sorted_array.append(arr[j])
        j += 1

    i = l1
    for element in sorted_array:
        arr[i] = element
        i += 1

    del sorted_array
    gc.collect()


def merge_sort(arr: [], low: int, high: int):
    if high > low:
        merge_sort(arr, low, int((high + low) / 2))
        merge_sort(arr, int((high + low) / 2) + 1, high)
        merge(arr, low, int((high + low) / 2), int((high + low) / 2) + 1, high)


arr = [rand(0, RANGE) for _ in range(LENGTH)]
print(arr)

print("-----------------------After Sorting------------------------")
merge_sort(arr, 0, (LENGTH - 1))
print(arr)
