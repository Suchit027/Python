# function to print common characters in two strings

def common(str1, str2):
    for i in str1:
        if i in str2:
            print(i, end=' ')
    return


def main():
    str1 = input('enter string 1')
    str2 = input('enter string 2')
    common(str1, str2)


if __name__ == '__main__':
    main()
