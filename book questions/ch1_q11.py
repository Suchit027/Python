print('Enter year')
myinput = input()
myinput = int(myinput)
if myinput % 4 == 0 and myinput % 100 == 0 and myinput % 400 == 0:
    print('Leap year')
else:
    print('Not a leap year')
