print('enter string')
str = input()
cw = cd = cu = cl = 0
for i in str:
    if i.isalpha():
        cw += 1
    if i.isnumeric():
        cd += 1
    if i.isupper():
        cu += 1
    if i.islower():
        cl += 1
print(cw, cd, cu, cl)
