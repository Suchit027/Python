import seaborn
from matplotlib import pyplot
import numpy

seaborn.set_style('whitegrid')

# creating a figure
fig = pyplot.figure()
# creating axes
ax = pyplot.axes()
# creating x-axis points
x = numpy.linspace(0, 10, 1000)
ax.plot(x, numpy.sin(x))
pyplot.plot(x, numpy.sin(x))
pyplot.plot(x, numpy.cos(x))

pyplot.xlim(0, 11)
pyplot.ylim(-2, 2)
# making the plot show only up until used limits
pyplot.axis('tight')
pyplot.title('Plotting data using sin and cos')
pyplot.show()
