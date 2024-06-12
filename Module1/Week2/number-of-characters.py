def count_chars(string):
    char_dct = {}
    for char in string:
        if char in char_dct:
            char_dct[char] += 1
        else:
            char_dct[char] = 1
    return char_dct


assert count_chars("Happiness") == {
    "H": 1,
    "a": 1,
    "p": 2,
    "i": 1,
    "n": 1,
    "e": 1,
    "s": 2,
}
assert count_chars("smiles") == {"s": 2, "m": 1, "i": 1, "l": 1, "e": 1}
