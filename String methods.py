import string

# to capitalize first character of the string
print(string.capwords("hello"))

# to count number of times a substring occurs from beginning to end of given index
# case matters
x = "hello"
print(x.count("EL", 0, len(x)))

# checks if the string ends with the given suffix
# case matters
print(x.endswith('O', 0, len(x)))

# finds the first index where substring is found in the string
# case matters
print(x.find('EL', 0, len(x)))

# checks if the string only has alphabets and numbers and must have at least one character
print(x.isalnum())

# checks if the string only has alphabets and must have at least one character
print(x.isalpha())

# checks if the string only has numbers and must have at least one character
print(x.isdigit())

# checks if the string has all lowercase letters
print(x.islower())

# checks if the string has all uppercase letters
print(x.isupper())

# checks if characters of string are whitespace
print(x.isspace())

# converts to lowercase
# it returns new string instead of changing the original one
print(x.lower())

# converts to uppercase
# it returns new string instead of changing the original one
print(x.upper())

# checks if the string starts with the substring from index 1 to index 2
# case matters
print(x.startswith('he', 0, len(x)))

# swaps case
print(x.swapcase())
