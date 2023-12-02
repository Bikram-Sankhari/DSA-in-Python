def find_max_min(arr):
    maximum = minimum = arr[0]
    for element in arr:
        if element < minimum:
            minimum = element

        if element > maximum:
            maximum = element

    return maximum, minimum


print(find_max_min([5, 3, 8, 1, 6, 9]))

"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)

"""
