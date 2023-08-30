def middle(string1, string2):
    lis = list(string1)
    length = len(lis)
    lis.insert(length // 2, string2)
    nstring = ''.join(lis)
    print(nstring)


def main():
    string1 = input('enter string1\n')
    string2 = input('enter string 2\n')
    middle(string1, string2)


if __name__ == '__main__':
    main()
