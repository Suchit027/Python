import numpy
from plotly import graph_objs
from matplotlib import pyplot

x = numpy.random.randn(2000)
y = numpy.random.randn(2000)
f = graph_objs.Figure(graph_objs.Histogram2dContour(x=x, y=y, contours=dict(coloring='heatmap')))
f.add_trace(graph_objs.Scatter(mode='markers',
                               x=x,
                               y=y,
                               marker=dict(color='white',
                                           size=3,
                                           opacity=0.3)))

f.show()
