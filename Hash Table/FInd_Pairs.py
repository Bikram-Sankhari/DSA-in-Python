def find_pairs(a1, a2, goal):
    a1 = set(a1)
    result = []
    for num in a2:
        if goal - num in a1:
            result.append((goal - num, num))
    return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)

"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""
