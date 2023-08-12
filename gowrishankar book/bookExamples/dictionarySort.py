def read():
    string = input()
    lis = string.split(' ')
    return lis


def sort(lis):
    for j in range(0, len(lis) - 1):
        for i in range(j, len(lis)):
            if lis[j] > lis[i]:
                temp = lis[j]
                lis[j] = lis[i]
                lis[i] = temp
    print('sorted')
    for i in lis:
        print(f'{i}')
    return


def main():
    print('enter string')
    sort(read())


if __name__ == '__main__':
    main()
