print('Enter age')
myinput = input()
myinput = int(myinput)
if myinput < 13:
    print('Child')
elif 13 <= myinput <= 17:
    print('Teenager')
elif 18 <= myinput <= 59:
    print('Adult')
else:
    print('Senior')