import pandas

numbers = ['10', '11', '12', '13']
# notice how index is created
series = pandas.Series(numbers, index=['A', 'B', 'C', 'D'])
print(series)

# the data is displayed in the order the keys are indexed
numbers2 = {'num1': '1', 'num2': '2', 'num3': '3'}
series2 = pandas.Series(numbers2, index=['num1', 'num3', 'num2'])
print(series2)

# changing series value
series2['num1'] = 10
print(series2)

# finding values from series index
# series.loc for labels
print(series['A'])
print(series.loc['A'])

numbers3 = ['num1', 'num2', 'num3']
series3 = pandas.Series(numbers3)
print(series3)

# series.iloc is used for index made of number
print(series3.iloc[1])
