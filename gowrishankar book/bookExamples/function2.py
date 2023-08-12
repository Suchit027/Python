def test(a):
    return a, a + 1


def main():
    a, b = test(1)
    print(a, b)


if __name__ == '__main__':
    main()
