from matplotlib import pyplot
import numpy
import seaborn
import pandas

seaborn.set_style('whitegrid')

data = numpy.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pandas.DataFrame(data, columns=['x', 'y'])

seaborn.displot(data['x'])
seaborn.displot(data['y'])
pyplot.show()

# for kernel density estimation
for col in 'xy':
    seaborn.kdeplot(data[col], fill=True)
pyplot.show()

# passing full 2 D data set to kdeplot
seaborn.kdeplot(data, x='x', y='y')
pyplot.show()

with seaborn.axes_style('white'):
    seaborn.jointplot(data=data, x='x', y='y', kind='kde')
pyplot.show()

with seaborn.axes_style('white'):
    seaborn.jointplot(data=data, x='x', y='y', kind='hex')
pyplot.show()
