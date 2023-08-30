def unique(sen):
    lis = sen.split(' ')
    set1 = set(lis)
    print(set1)


def main():
    sen = input('enter the string\n')
    unique(sen)


if __name__ == '__main__':
    main()
