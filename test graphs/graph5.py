from matplotlib import pyplot
import seaborn
import numpy
import pandas

seaborn.set_style('whitegrid')
data = numpy.random.multivariate_normal(mean=[0, 0], cov=[[5, 2], [2, 2]], size=2000)
data = pandas.DataFrame(data=data, columns=['x', 'y'])

seaborn.displot(data['x'])
seaborn.displot(data['y'])
pyplot.show()

seaborn.kdeplot(data['x'], fill=True)
seaborn.kdeplot(data['y'], fill=True)
pyplot.show()

seaborn.kdeplot(data, x='x', y='y')
pyplot.show()

seaborn.jointplot(data, x='x', y='y', kind='kde')
pyplot.show()

seaborn.jointplot(data, x='x', y='y', kind='hex')
pyplot.show()
