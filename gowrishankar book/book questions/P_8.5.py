def sort(sen):
    lis = []
    tup = sen.split(' ')
    for i in tup:
        lis.append((i, len(i)))
    lis.sort(reverse=True)
    print(lis)


def main():
    sen = input('enter the sentence\n')
    sort(sen)


if __name__ == '__main__':
    main()
