import pandas
import numpy
from matplotlib import pyplot

data = pandas.DataFrame(numpy.random.randn(200, 6), index=pandas.date_range('1/9/2009', periods=200),
                        columns=list('ABCDEF'))
data.plot(kind='line')
pyplot.show()
