import numpy
import pandas
from matplotlib import pyplot

data = pandas.DataFrame(data=numpy.random.randn(200, 4),
                        columns=['a', 'b', 'c', 'd'])

data.plot(kind='scatter', x='a', y='b')
pyplot.show()
