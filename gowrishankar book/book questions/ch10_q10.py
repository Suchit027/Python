import re


def correct(num):
    pattern = re.compile(r'0*(\d+)')
    final = pattern.match(num)
    final = final.group(1)
    print(final)


def main():
    num = input('enter number ')
    correct(num)


if __name__ == '__main__':
    main()
