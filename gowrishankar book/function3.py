def add_cubes(a, b):
    def surfarea(a):
        return 6 * (a ** 2)

    return surfarea(a) + surfarea(b)


def main():
    print(add_cubes(1, 2))


if __name__ == '__main__':
    main()
