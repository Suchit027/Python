import seaborn
from matplotlib import pyplot

# loading existing dataset
dataset = seaborn.load_dataset('tips')

# regular plotting; naming x and y-axis and specifying data
seaborn.regplot(x='total_bill', y='tip', data=dataset)
pyplot.xlabel = 'Total Bill'
pyplot.ylabel = 'Bill Tips'
pyplot.show()
