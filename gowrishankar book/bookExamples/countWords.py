print('enter sentence')
sen = input()
print('enter word')
wor = input()
count = 0
for i in range(0, len(sen)):
    if wor == sen[i: i + len(wor)]:
        count += 1
print(count)
