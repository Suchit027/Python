import pandas
import numpy

data = numpy.array([90, 75, 50, 66])
s = pandas.Series(data, index=['a', 'b', 'c', 'd'])
print(s)

data = {'Akshay': 92, 'Aakash': 55, 'Aman': 83}
s = pandas.Series(data, index=['Akshay', 'Aakash', 'Aman'])
print(s)

# no need to put index for dictionary
# index only needed if order of dictionary is to be changed
f = pandas.Series(data=data)
print(f)
