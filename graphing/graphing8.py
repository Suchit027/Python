import numpy
import pandas
from matplotlib import pyplot

data = pandas.DataFrame(data=numpy.random.randn(20, 5),
                        columns=['Jan', 'Feb', 'March', 'Apr', 'May'])
data.plot(kind='bar', stacked=True)

pyplot.show()
