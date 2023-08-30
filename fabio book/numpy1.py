import numpy
import numpy as np

a = numpy.array([1, 2, 3, 4])
print(a)
a = numpy.array([[1, 2, 3], [4, 5, 6]])
print(a)
a = numpy.array((1, 2, 3), dtype=complex)
print(a)
a = numpy.zeros((4, 4))
print(a)
a = numpy.ones((2, 2))
print(a)
a = numpy.arange(0, 5)
print(a)
a = numpy.arange(0, 6, 2)
print(a)
a = numpy.arange(0, 8).reshape(2, 4)
print(a)
a = numpy.linspace(0, 10, 3)
print(a)
a += 3
print(a)
print(numpy.sqrt(a))
a = numpy.random.random(8).reshape(2, 4)
print(a)
b = numpy.random.random(8).reshape(2, 4)
print(b)
print(a * b)
print(a[:, 1])
for row in a:
    print(row)
print(a < 5)
a = numpy.random.random(5)
print(a)
b = numpy.random.random(10).reshape(2,5)
print(b)
print(a + b)