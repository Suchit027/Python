import re


def main():
    string = input('enter date ')
    pattern = re.compile(r'(\d{4})/(\d{2})/(\d{2})')
    test = pattern.sub(r'\3/\2/\1', string)
    print(test)


if __name__ == '__main__':
    main()
