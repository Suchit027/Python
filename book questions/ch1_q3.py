import random

print('Enter first and last values')
myinput = input()
list = myinput.split()

# randint returns random integer between both end points
print(random.randint(int(list[0]), int(list[1])))

# returns a list with specified number of samples of random integers between the endpoints including the endpoints
print(random.sample(range(int(list[0]), int(list[1])), 1))
