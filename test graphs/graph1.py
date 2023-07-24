import seaborn
from matplotlib import pyplot
import pandas

# you need dataframes to create regplots
data = {'x': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'y': [11, 12, 13, 14, 15, 16, 17, 18, 19]}
data = pandas.DataFrame(data=data, columns=['x', 'y'])
seaborn.regplot(data=data, x='x', y='y')
pyplot.xlim(0, 10)
pyplot.ylim(0, 20)
pyplot.xlabel = 'X axis'
pyplot.ylabel = 'Y axis'
pyplot.show()
