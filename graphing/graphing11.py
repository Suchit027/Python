import numpy
import pandas
from matplotlib import pyplot

data = pandas.DataFrame(data={'A': numpy.random.randn(200),
                              'B': numpy.random.randn(200),
                              'C': numpy.random.randn(200)},
                        columns=['A', 'B', 'C'])
data.plot(kind='hist', bins=20, subplots= True)
pyplot.show()
