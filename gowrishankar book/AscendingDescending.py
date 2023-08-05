print('enter numbers')
my = input()
lis = my.split(' ')
for i in range(len(lis)):
    lis[i] = int(lis[i])
ascending = descending = 0
for i in range(len(lis) - 1):
    if lis[i] <= lis[i + 1]:
        ascending = 1
    else:
        descending = 1
if ascending == 1 and descending == 1:
    print('not sorted')
elif ascending == 1:
    print('ascending')
else:
    print('descending')
