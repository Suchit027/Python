def striping(string, char):
    string = string.strip(char)
    print(string)


def main():
    string1 = input('enter string ')
    string2 = input('enter characters ')
    striping(string1, string2)


if __name__ == '__main__':
    main()
