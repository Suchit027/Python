import seaborn
from matplotlib import pyplot

dataset = seaborn.load_dataset('tips')
seaborn.regplot(x='total_bill', y='tip', data=dataset)
pyplot.xlabel = 'Total Bill'
pyplot.ylabel = 'Bill Tips'
pyplot.show()
