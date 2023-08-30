def make(n):
    n = int(n)
    dic = dict()
    for i in range(0, n):
        print('enter name')
        name = input()
        print('enter reg and marks')
        reg, marks = input().split(' ')
        dic[name] = [reg, marks]
    return dic


def call(name, dic):
    print(f'reg. no = {dic[name][0]} marks = {dic[name][1]}')


def main():
    n = input('enter n ')
    dic = make(n)
    name = input('enter name ')
    call(name, dic)


if __name__ == '__main__':
    main()
