def edit(string):
    lis = list(string)
    for i in range(len(lis)):
        if lis[i] == 'a' or lis[i] == 'e' or lis[i] == 'i' or lis[i] == 'o' or lis[i] == 'u':
            lis[i] = ''
    nstring = ''.join(lis)
    return nstring


def main():
    print('enter string')
    string = input()
    nstring = edit(string)
    print(nstring)


if __name__ == '__main__':
    main()
