import numpy as np


def group_anagrams(words):
    grouped_anagrams = {}
    for word in words:
        word_combination = np.zeros(26)
        for letter in word:
            position = ord(letter) - 97
            word_combination[position] += 1
        final_combination = word_combination.tobytes()
        if final_combination in grouped_anagrams:
            grouped_anagrams[final_combination].append(word)
        else:
            grouped_anagrams[final_combination] = [word]

    return [value for value in grouped_anagrams.values()]


print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))

"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""
