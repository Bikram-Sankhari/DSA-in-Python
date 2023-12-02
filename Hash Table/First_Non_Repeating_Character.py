def first_non_repeating_char(string):
    temp = {}
    for character in string:
        if character in temp:
            temp[character] += 1
        else:
            temp[character] = 1

    for character in string:
        if temp[character] == 1:
            return character

    return None


print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
