print('enter first number')
a = input()
if a == 'done':
    print('no number to check')
lis = [a]
while a != 'done':
    print(max(lis))
    a = input()
    lis.append(a)
