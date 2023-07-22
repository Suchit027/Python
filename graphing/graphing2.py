import seaborn
from matplotlib import pyplot

dataset = seaborn.load_dataset('iris')
seaborn.pairplot(dataset, kind='scatter')
pyplot.show()
