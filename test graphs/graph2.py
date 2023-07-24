import pandas
import seaborn
from matplotlib import pyplot

data = {'Name': ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b'], 'col1': [1, 2, 3, 4, 5, 6, 7, 8],
        'col2': [11, 22, 33, 44, 55, 66, 77, 88],
        'col3': [11, 12, 13, 14, 15, 16, 17, 18]}
data = pandas.DataFrame(data=data)
seaborn.pairplot(data=data, hue='Name', kind='scatter')
pyplot.show()
