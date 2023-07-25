import numpy
import pandas
from matplotlib import pyplot

data = pandas.DataFrame(data={'a': numpy.random.randint(low=0, high=1000, size=200),
                              'b': numpy.random.randint(low=0, high=1000, size=200),
                              'c': numpy.random.randint(low=0, high=1000, size=200),
                              'd': numpy.random.randint(low=0, high=1000, size=200)})

data.plot(kind='area')
pyplot.show()
