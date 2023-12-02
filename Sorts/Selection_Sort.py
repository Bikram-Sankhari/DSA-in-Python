def selection_sort(arr):
    for iteration_count in range(len(arr) - 1):
        min_index = iteration_count
        for element_count in range(iteration_count + 1, len(arr)):
            if arr[min_index] > arr[element_count]:
                min_index = element_count

        if min_index != iteration_count:
            arr[min_index], arr[iteration_count] = arr[iteration_count], arr[min_index]

    return arr


print(selection_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]

 """
