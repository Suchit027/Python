def count(lis):
    dic = dict()
    for i in lis:
        dic[i] = dic.get(i, 0) + 1
    skeys = sorted(dic)
    for i in skeys:
        print(f'{i} = {dic.get(i)}')


def main():
    lis = input('enter string\n')
    lis = list(lis)
    count(lis)


if __name__ == '__main__':
    main()
