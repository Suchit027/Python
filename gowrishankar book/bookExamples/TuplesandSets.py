# creating tuples
tup1 = 1,
tup1 = 1, 2, 3
print(tup1)

# basic tuple operations
tup2 = tup1 * 3
print(tup2)
tup2 = tup1 + tup1
print(tup2)

# 'in' in tuples
print(2 in tup2)

# tuples from strings
tup3 = tuple('hi')
tup4 = (1, 2, 3, 4, 5)
print(tup3)
print(tup4)

# sum in tuples
# no display for this
# print(sum(tup3))
print(sum(tup4))

# modifying tuples
tup5 = (1, 2, 3, 4, [5, 6])
print(tup5)
tup5[4][1] = 7
print(tup5)

# count and index in tuples
print(tup4.count(2))
print(tup4.index(3))

# updating tuples
tup6 = 1, 2
tup6 += 3,
print(tup6)

# can't delete elements from a tuple

