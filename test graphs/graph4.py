import numpy
import seaborn
from matplotlib import pyplot

seaborn.set_style('whitegrid')
X = numpy.linspace(0, 10, 1000)


pyplot.figure()
pyplot.plot(X, numpy.tan(X))
pyplot.plot(X, numpy.cos(X))

pyplot.xlim(0, 11)
pyplot.ylim(-50, 50)

pyplot.xlabel('x axis')
pyplot.ylabel('y axis')
pyplot.title('test graph')
pyplot.show()
