def remove_element(arr, val):
    index, length = 0, len(arr)
    while index < length:
        if arr[index] == val:
            arr.pop(index)
            length -= 1
        else:
            index += 1
    return len(arr)


# Test case 1: Removing a single instance of a value (1) in the middle of the list.
nums1 = [2, 1, 1, 1]
val1 = 1
print("\nRemove a single instance of value", val1, "in the middle of the list.")
print("BEFORE:", nums1)
new_length1 = remove_element(nums1, val1)
print("AFTER:", nums1, "\nNew length:", new_length1)
print("-----------------------------------")
