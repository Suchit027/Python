import re

'''def main():
    with open('secret_societies.txt') as file:
        pattern = re.compile(r'(\w\s)(\s\w)')
        for i in file:
            print(pattern.sub(r'\2 \1', i))


if __name__ == '__main__':
    main()'''


def main():
    with open('secret_societies.txt') as file:
        string = file.readlines()
        for i in string:
            i = i.rstrip()
            lis = list(i)
            lis.reverse()
            print(''.join(lis))


if __name__ == '__main__':
    main()
