def count(lis):
    dic = dict()
    for i in lis:
        dic[i] = dic.get(i, 0) + 1
    print(dic)


def main():
    lis = input('enter list\n')
    count(lis)


if __name__ == '__main__':
    main()
