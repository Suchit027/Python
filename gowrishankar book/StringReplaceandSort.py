print('enter string')
string = input()
newString = string.replace(',', '-')
print(newString)
lis = newString.split('-')
for i in range(len(lis)):
    for j in range(i + 1, len(lis)):
        if lis[i] > lis[j]:
            temp = lis[i]
            lis[i] = lis[j]
            lis[j] = temp
print(lis)
