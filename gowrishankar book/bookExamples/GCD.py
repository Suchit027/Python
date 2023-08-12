print('Enter the number 1')
a = int(input())
print('Enter number 2')
b = int(input())
c = b
while c != 0:
    if b % c == 0 and a % c == 0:
        break
    c -= 1
print(f'GCD is {c}')
