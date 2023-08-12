print('enter word')
wor = input()
print('enter amount')
rot = int(input())
lis = []
for i in range(0, len(wor)):
    # notice chr for conversion to char from ascii
    # notice ord for getting ascii of char
    lis.append(chr(ord(wor[i]) + rot))
newstring = ''.join(lis)
print(newstring)
