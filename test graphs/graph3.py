import seaborn
from matplotlib import pyplot

seaborn.set_style('whitegrid')
X = [100, 123, 154, 145, 176, 254, 265, 321, 421, 789]
Y = [12, 43, 53, 76, 23, 87, 18, 98, 34, 21]

pyplot.scatter(X, Y, s=60, c='blue', marker='+')
pyplot.xlabel('X axis')
pyplot.ylabel('Y axis')
pyplot.title('test graph')
pyplot.xlim(0, 1000)
pyplot.ylim(0, 100)
pyplot.show()
