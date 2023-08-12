def sort(string):
    lis = string.split(" ")
    word = []
    for i in lis:
        word.append((len(i), i))
    word.sort()
    print('sorted')
    for length, sample in word:
        print(f'{sample}  {length}')
    return


def main():
    print('enter the words')
    string = input()
    sort(string)


if __name__ == '__main__':
    main()
