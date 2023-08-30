import re


def main():
    string = input('enter string ')
    pattern = re.compile(r'(\d{1,3})')
    test = pattern.findall(string)
    print(test)


if __name__ == '__main__':
    main()
