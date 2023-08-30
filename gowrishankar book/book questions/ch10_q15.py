import re


def main():
    sen = input('enter string ')
    pattern = re.compile(r'(Street)\w*')
    test = pattern.sub('St.', sen)
    print(test)


if __name__ == '__main__':
    main()
