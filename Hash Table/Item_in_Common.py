def item_in_common(l1, l2):
    temp = {}
    for item in l1:
        temp[item] = True

    for item in l2:
        if item in temp:
            return True

    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))

"""
    EXPECTED OUTPUT:
    ----------------
    True

"""
