try:
    a = int(input())
    ls = [a]
    while a != 'done':
        a = int(input())
        ls.append(a)
except ValueError:
    a = 0
# else only executed if everything in try goes well
else:
    avg = sum(ls) / len(ls)
    print(avg)
finally:
    print('end')
