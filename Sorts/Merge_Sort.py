def merge_sort(arr):
    def inner_merge_sort(arr, low, high):
        if low == high:
            return

        inner_merge_sort(arr, low, (low + high) // 2)
        inner_merge_sort(arr, ((low + high) // 2) + 1, high)
        merge(arr, low, (low + high) // 2, ((low + high) // 2) + 1, high)

    def merge(arr, l1, h1, l2, h2):
        sorted_array = []
        i, j = l1, l2

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

    inner_merge_sort(arr, 0, len(arr) - 1)


a = [2, 1, 3, 5, 2, 3]
merge_sort(a)
print(a)
