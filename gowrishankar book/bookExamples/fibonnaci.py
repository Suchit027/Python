print('enter number')
a = int(input())
fib = [0, 1]
index = 0
while a - 2 > 0:
    fib.append(fib[index] + fib[index + 1])
    index += 1
    a -= 1
print(fib)
