import numpy
import pandas
from matplotlib import pyplot

data = pandas.DataFrame(numpy.random.randn(20, 5), columns=['A', 'B', 'C', 'D', 'E'])
# bins mean number of intervals on the x-axis
data.plot(kind='hist', bins=10)
pyplot.show()
