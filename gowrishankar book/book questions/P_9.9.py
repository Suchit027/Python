def main():
    string = input('enter file name ')
    lis = []
    with open(string, 'r') as file:
        longest = ''
        for row in file:
            wordlist = row.rstrip().split()
            for each in wordlist:
                if len(each) > len(longest):
                    longest = each
    print(longest)


if __name__ == '__main__':
    main()
