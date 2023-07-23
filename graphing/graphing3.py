import seaborn
from matplotlib import pyplot

# style of graph-sheet
seaborn.set_style('whitegrid')

# making x and y entries
X = [590, 540, 740, 130, 810, 300, 320, 230, 470, 620, 770, 250]
Y = [32, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]

# creating the plot
pyplot.scatter(X, Y)

# setting limits of the graph
pyplot.xlim(0, 1000)
pyplot.ylim(0, 100)

# plot created again and superimposed
# s= size
# c= color
# marker= the style of dots
pyplot.scatter(X, Y, s=60, c='red', marker='^')
pyplot.xlim(0, 1000)
pyplot.ylim(0.100)

# creating title of the graph
pyplot.title('Relationship between temperature and iced coffee sales')

# Naming x and y axis
pyplot.xlabel('Sold Coffee')
pyplot.ylabel('Temperature in Fahrenheit')

# showing the graph
pyplot.show()
