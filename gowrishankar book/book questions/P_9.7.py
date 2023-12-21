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
        for i in file:
            i = i.rstrip()
            i = i[::-1]
            print(i)


if __name__ == '__main__':
    main()
