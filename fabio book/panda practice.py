import pandas

frame = pandas.DataFrame({'color': ['white', 'red', 'green', 'red', 'green'],
                          'object': ['pen', 'pencil', 'pencil', 'ashtray', 'pen'],
                          'price1': [5.56, 4.20, 1.30, 0.56, 2.75],
                          'price2': [4.75, 4.12, 1.60, 0.75, 3.15]})
gg = frame['price1'].groupby([frame['color'], frame['object']])
print(gg.sum())