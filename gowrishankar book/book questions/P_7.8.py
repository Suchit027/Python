def count(sent):
    dic = {'dig': 0, 'upp': 0, 'low': 0}
    lis = list(sent)
    for i in lis:
        if i.isdigit():
            dic['dig'] += 1
        if i.islower():
            dic['low'] += 1
        if i.isupper():
            dic['upp'] += 1
    print(dic)


def main():
    sen = input('enter the sentence\n')
    count(sen)


if __name__ == '__main__':
    main()
