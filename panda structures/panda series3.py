import pandas
import numpy

# slicing series
data = [1, 2, 3, 4, 5]
f = pandas.Series(data=data)
print(f.get(2))
print(f[1:3])

# data greater than its mean
print(f.mean())
print(f[f > f.mean()])
# data greater than its median
print(f.median())
print(f[f > f.median()])
# e^x of data
print(numpy.exp(f))

# creating scalar series
f2 = pandas.Series(1, index=[0, 1, 2, 3, 4])
print(f2)
print(f2.index)

# vector operations and label alignment
# addition
print(f + f2)
print(f[1:] + f2[:-1])
# multiplication
print(f * f2)

# naming series
f3 = pandas.Series([1, 2, 3, 4, 5], name='test')
print(f3.name)
f3.name = 'update'
print(f3.name)
f3 = f3.rename('update2')
print(f3.name)
