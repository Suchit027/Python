celsius = [39.2, 36.5, 37.3, 37.8]
# notice map
Fahrenheit = map(lambda y: (9 / 5) * y + 32, celsius)
for x in Fahrenheit:
    print(x)
