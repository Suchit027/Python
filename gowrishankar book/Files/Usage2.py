def read_file():
    print('starting')
    with open(r'C:\Users\Suchit\Desktop\Python\Python_book\gowrishankar book\Files\Japan.txt', 'r') as file:
        for each in file:
            print(file.read(), end='')


def main():
    read_file()


if __name__ == '__main__':
    main()
