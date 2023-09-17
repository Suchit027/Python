def main():
    with open('quotes.txt') as file:
        dic = dict()
        for i in file:
            i = i.rstrip()
            lis = i.split(' ')
            for j in lis:
                dic[j] = dic.get(j, 0) + 1
        print(dic)
        lis2 = dic.values()
        print(f'no. of words = {sum(lis2)}')


if __name__ == '__main__':
    main()
