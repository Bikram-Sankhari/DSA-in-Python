def quick_sort(arr: list[int]):
    def inner_quick_sort(arr, low, high):
        if low >= high:
            return

        pivot = fit(arr, low, high)
        inner_quick_sort(arr, low, pivot - 1)
        inner_quick_sort(arr, pivot + 1, high)

    def fit(arr, low, high):
        i, j = low + 1, high

        while i < j:
            while i < high and arr[i] <= arr[low]:
                i += 1

            while arr[j] > arr[low]:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        if arr[j] < arr[low]:
            arr[low], arr[j] = arr[j], arr[low]

        return j

    inner_quick_sort(arr, 0, len(arr) - 1)
    return arr


print(quick_sort([6, 1, 2, 3, 9]))
