def find_duplicates(l):
    temp_dict = {}
    result = []
    for item in l:
        if item in temp_dict:
            result.append(item)
        else:
            temp_dict[item] = True

    return result


print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))

"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""
