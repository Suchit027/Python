print('enter number')
a = int(input())
sumE = sumO = 0
for i in range(0, a + 1, 2):
    sumE += i
for i in range(1, a + 1, 2):
    sumO += i
print(f'{sumE} and {sumO}')
