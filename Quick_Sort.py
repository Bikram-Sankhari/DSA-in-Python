from random import randint as rand

RANGE = 10
LENGTH = 5


def partition(arr: [], low: int, high: int) -> int:
    i = low + 1
    j = high

    while j > i:
        while arr[i] <= arr[low] and i < high:
            i += 1

        while arr[j] > arr[low]:
            j -= 1

        if j > i:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    if arr[j] < arr[low]:
        temp = arr[j]
        arr[j] = arr[low]
        arr[low] = temp

    return j


def quick_sort(arr: [], low: int, high: int):
    if high > low:
        n = partition(arr, low, high)
        quick_sort(arr, low, (n-1))
        quick_sort(arr, (n + 1), high)


arr = [rand(0, RANGE) for _ in range(LENGTH)]
print(arr)

print("-----------------------After Sorting------------------------")
quick_sort(arr, 0, (LENGTH - 1))
print(arr)
