def common(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    set3 = set1.intersection(set2)
    print(set3)


def main():
    str1 = input('enter string one ')
    str2 = input('enter string 2 ')
    common(str1, str2)


if __name__ == '__main__':
    main()
