def find_longest_string(arr):
    longest_string = ''
    length_of_longest_string = 0

    for element in arr:
        if len(element) > length_of_longest_string:
            longest_string = element
            length_of_longest_string = len(longest_string)

    return longest_string


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)

"""
    EXPECTED OUTPUT:
    ----------------
    banana

"""
