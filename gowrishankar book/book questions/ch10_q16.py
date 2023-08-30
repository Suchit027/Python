import re


def main():
    pattern = re.compile(r'\w{5}')
    sen = input('enter string ')
    lis = pattern.findall(sen)
    print(lis)


if __name__ == '__main__':
    main()
