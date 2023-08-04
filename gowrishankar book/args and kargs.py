def cheese_shop(kind, *args, **kwargs):
    print(f'do you have any {kind}')
    print(f'i am sorry we are all out of {kind}')
    for arg in args:
        print(arg)
    print('-' * 10)
    for kw in kwargs:
        print(kw + ':' + kwargs[kw])


def main():
    cheese_shop('Limburger', 'it is very runny', 'it is runnier', shopkeeper='Michael Palin',
                client='John Clees', sketch='cheese sketch shop')


if __name__ == '__main__':
    main()
