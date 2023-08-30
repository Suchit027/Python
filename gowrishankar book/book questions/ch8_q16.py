def create(n):
    n = int(n)
    lis = []
    for i in range(1, n + 1):
        lis.append((i, i ** 2))
    print(lis)


def main():
    n = input('enter n\n')
    create(n)


if __name__ == '__main__':
    main()
