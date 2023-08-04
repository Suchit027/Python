print('enter number')
a = int(input())
for i in range(1, a + 1):
    for j in range(1, i + 1):

        # notice end
        print(i, end='')
    for k in range(1, (a * 2) - (i * 2)):
        print(' ', end='')
    for p in range(1, i + 1):
        print((i + 1 - p), end='')
    print('\n')
