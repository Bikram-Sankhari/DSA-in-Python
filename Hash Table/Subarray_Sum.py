def subarray_sum(num_arr, goal):
    my_dick = {0: -1}
    running_sum = 0
    for index, num in enumerate(num_arr):
        running_sum += num
        if (running_sum - goal) in my_dick:
            return [my_dick[running_sum - goal] + 1, index]
        my_dick[running_sum] = index

    return []


nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
