import numpy
import pandas
from matplotlib import pyplot

data = pandas.DataFrame(data=numpy.random.randn(20, 5),
                        columns=['A', 'B', 'C', 'D', 'E'])
data.plot(kind='barh', stacked=True)
pyplot.show()
