def bubble_sort(arr):
    iteration_count = len(arr) - 1
    while iteration_count > 0:
        element_count = 0
        while element_count < iteration_count:
            if arr[element_count] > arr[element_count + 1]:
                arr[element_count], arr[element_count + 1] = arr[element_count + 1], arr[element_count]
            element_count += 1

        iteration_count -= 1

    return arr


print(bubble_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]

 """