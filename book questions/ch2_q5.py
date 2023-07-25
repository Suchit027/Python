import pandas
from matplotlib import pyplot

salesMen = ['A', 'B', 'C', 'D', 'E', 'F']
Mobile_Sales = [2540, 1370, 1320, 2000, 2100, 2150]
TV_Sales = [2200, 1900, 2150, 1850, 1770, 2000]
data = pandas.DataFrame()
data['Name'] = salesMen
data['Mobile_Sales'] = Mobile_Sales
data['TV_Sales'] = TV_Sales

# the first argument sets the index as that column
# drop hides the newly created index
# inplace updates the dataframe instead of creating a new one
data.set_index('Name', drop=True, inplace=True)
print(data)

data.plot(kind='bar')
pyplot.show()

# subplots needed
data.plot(kind='pie', subplots=True)
pyplot.show()

data.plot(kind='box')
pyplot.show()

data.plot(kind='area')
pyplot.show()

data.plot(kind='bar', stacked=True)
pyplot.show()
