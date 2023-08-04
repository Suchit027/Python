try:
    print('enter a number')
    # for ValueError
    a = int(input())
    print(f'entered number {a}')
    b = int(input())
    # for ZeroDivisionError
    c = a / b
except ValueError:
    print('not a number')
else:
    print('when no exception is raised')
finally:
    print('end')
