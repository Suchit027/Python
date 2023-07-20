print('How many terms needed')
myinput = input()
myinput = int(myinput)

if myinput < 0:
    print('error')
    exit()

list = []
for i in range(1, myinput + 1):
    if i == 1:
        list.append(0)
    if i == 2:
        list.append(1)
    if i > 2:
        list.append(list[len(list) - 1] + list[len(list) - 2])

print('Series =', list)
