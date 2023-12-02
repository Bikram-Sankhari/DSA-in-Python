def insertion_sort(arr):
    for iteration_count in range(1, len(arr)):
        current_value = arr[iteration_count]
        for element_count in range(iteration_count - 1, -1, -1):
            if arr[element_count] > current_value:
                arr[element_count + 1], arr[element_count] = arr[element_count], arr[element_count + 1]

    return arr


print(insertion_sort([2, 1, 3, 4, 5, 6]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]

 """
