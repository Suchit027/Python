def removing(string):
    lis = list(string)
    for i in range(0, len(lis)):
        if lis[i] == 'a' or lis[i] == 'e' or lis[i] == 'o' or lis[i] == 'u' or lis[i] == 'i':
            lis[i] = ''
    string = ''.join(lis)
    print(string)


def main():
    string = input('enter string\n')
    removing(string)


if __name__ == '__main__':
    main()
