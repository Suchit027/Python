dict1 = {'a': 1, 'b': 2, 'c': 3}

# updating dictionary
dict1['d'] = 4
print(dict1)

dict2 = {'Aman': 1000, 'Rahul': 200, 'Raju': 3000}
f = lambda x: x * 0.95
print('Name\tNet Salary')

# notice how the dictionary members are accessed
for key, value in dict2.items():
    # notice printing methods
    print(key, '\t', f(value))

# deleting dictionaries
del dict1['a']
print(dict1)
# deletes entire dictionary
del dict1
# all entries deleted
dict2.clear()
print(dict2)

dict1 = {'a': 1, 'b': 2, 'c': 3}
# length of dictionary
print(len(dict1))

# string representation of dictionary
print(str(dict1))
# returning type of variable
print(type(dict1))

# copying dictionary
dict3 = dict1.copy()
print(dict3)

# creating new dictionary form keys; values will be declared as None
seq = ('x', 'y', 'z')
dict4 = dict1.fromkeys(seq)
print(dict4)

# getting values
print(dict1.get('a'))

# checking if key is present
print('b' in dict1)

# returns key value tuple
print(dict1.items())

# displaying keys and values individually
print(dict1.keys())
print(dict1.values())

# finds key but will set key to default if not found
print(dict1.setdefault('d'))
print(dict1)
print(dict2)

# extending dictionaries
dict1.update(dict2)
print(dict1)

# sorting dictionaries
# by key
i = 5
for key in dict1:
    dict1[key] = i
    i -= 1
for k in sorted(dict1):
    print(k, dict1[k])
# by value
for k in sorted(dict1, key=dict1.get):
    print(k, dict1[k])
# for reversing order
for k in sorted(dict1, key=dict1.get, reverse=True):
    print(k, dict1[k])

