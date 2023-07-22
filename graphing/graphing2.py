import seaborn
from matplotlib import pyplot

dataset = seaborn.load_dataset('iris')

# pairwise comparison
seaborn.pairplot(dataset, kind='scatter')
pyplot.show()
