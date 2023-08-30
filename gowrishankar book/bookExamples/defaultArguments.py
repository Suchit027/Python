def test(one, two="hello"):
    print(f'{one} {two}')


def main():
    test('hi', 'bye')


if __name__ == '__main__':
    main()
