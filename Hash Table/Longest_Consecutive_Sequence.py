def longest_consecutive_sequence(arr):
    all_nums = set(arr)
    found_in_sequence = set()
    result = 0

    for number in arr:
        if number not in found_in_sequence:
            current_length = 1
            while number + 1 in all_nums:
                current_length += 1
                found_in_sequence.update([number, number + 1])
                number += 1
            if current_length > result:
                result = current_length

    return result


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
