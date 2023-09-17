def main():
    with open("Egypt.txt", "r") as file:
        lis = file.readlines()
        for i in lis:
            print(i, end='')


if __name__ == '__main__':
    main()
