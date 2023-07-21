# notice how using . before f below rounds of 3.1454 to 3.15
print("The of value of %s is = %.2f" % ("pi", 3.1454))

# notice how brackets and .format is used for indexing string and printing
x = "price is"
print("{1} {0} {2}".format(x, "The", 1920))


# another way to print
# notice how class is written
class A:
    x = 9


w = A()
# notice list and dictionary usage
print("{0} {1[2]} {2[test]} {3.x}".format("This", ["a", "or", "is"], {"test": "another"}, w))

# another way to print from a dictionary
print("Hi %(Name)s, your height is %(height).2f" % {'Name': 'Rahul', 'height': 172.5256})

# another way
name = 'Rahul'
age = '22'
age = int(age) + 1
print('Name: %s' % name, '\t age:%d' % age)
