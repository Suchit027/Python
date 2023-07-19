fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    # notice how it prints
    print(index, letter)
    # ++index doesn't work in python; only use proper expressions
    index += 1
