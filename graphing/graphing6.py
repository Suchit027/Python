from plotly import graph_objs
import numpy

# creating 2000 data set points
x = numpy.random.randn(2000)
y = numpy.random.randn(2000)

# creating a heatmap
fig = graph_objs.Figure(
    graph_objs.Histogram2dContour(x=x, y=y,
                                  contours={'coloring': 'heatmap'},
                                  ))

# adding points to the heatmap
fig.add_trace(graph_objs.Scatter(mode='markers',
                                 x=x,
                                 y=y,
                                 marker=dict(color='white',
                                             size=3,
                                             opacity=0.3)))
fig.show()
