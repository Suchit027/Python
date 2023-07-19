from functools import reduce

f = lambda a, b: a if (a > b) else b
print(reduce(f, [1, 2, 3, 4, 6, 5]))
