def read_file():
    print('starting')
    with open(r'C:\Users\Suchit\Desktop\Python\Python_book\gowrishankar book\Files\File1.txt', 'r') as file1, open(
            r'C:\Users\Suchit\Desktop\Python\Python_book\gowrishankar book\Files\Japan.txt', 'r') as file2:
        for each in file1:
            print(each, end='')
        for each in file2:
            print(each, end='')


def main():
    read_file()


if __name__ == '__main__':
    main()
