import random


def find_kth_smallest(num_array, k):
    random.shuffle(num_array)
    low, high = 0, len(num_array) - 1
    while low < high:
        j = partition(num_array, low, high)
        if j < k - 1:
            low = j + 1
        elif j > k - 1:
            high = j - 1
        else:
            break
    return num_array[k - 1]


def partition(num_array, low, high):
    i = low + 1
    j = high

    while i < j:
        while num_array[i] <= num_array[low] and i < high:
            i += 1

        while num_array[j] > num_array[low]:
            j -= 1

        if j > i:
            num_array[i], num_array[j] = num_array[j], num_array[i]

    if num_array[low] > num_array[j]:
        num_array[low], num_array[j] = num_array[j], num_array[low]
    return j


# Test cases
nums = [[3, 2, 1, 5, 6, 4], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [3, 2, 3, 1, 2, 4, 5, 5, 6]]
ks = [2, 3, 4, 7]
expected_outputs = [2, 3, 4, 5]

for i in range(len(nums)):
    print(f'Test case {i + 1}...')
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_smallest(nums[i], ks[i])
    print(f'Output: {result}')
    print(f'Expected output: {expected_outputs[i]}')
    print(f'Test passed: {result == expected_outputs[i]}')
    print('---------------------------------------')

# print(find_kth_smallest([2, 1, 5, 4, 6, 3], 3))
"""
    EXPECTED OUTPUT:
    ----------------
    Test case 1...
    Input: [3, 2, 1, 5, 6, 4] with k = 2
    Output: 2
    # Expected output: 2
    Test passed: True
    # ---------------------------------------
    # Test case 2...
    # Input: [6, 5, 4, 3, 2, 1] with k = 3
    Output: 3
    Expected output: 3
    Test passed: True
    ---------------------------------------
    Test case 3...
    Input: [1, 2, 3, 4, 5, 6] with k = 4
    Output: 4
    Expected output: 4
    Test passed: True
    ---------------------------------------
    Test case 4...
    Input: [3, 2, 3, 1, 2, 4, 5, 5, 6] with k = 7
    Output: 5
    Expected output: 5
    Test passed: True
    ---------------------------------------

"""
