def unique(*args):
    for i in args:
        print(f'unique letters in {i} = {set(i)}')


def main():
    unique("egg", "immune", "feed", "vacuum", "goddessship")


if __name__ == '__main__':
    main()
