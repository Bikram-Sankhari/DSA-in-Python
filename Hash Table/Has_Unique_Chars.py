def has_unique_chars(string):
    found_letters = set()
    for letter in string:
        if letter in found_letters:
            return False
        found_letters.add(letter)

    return True




print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""