def main():
    with open('Sample_program.py', 'r') as file:
        for i in file:
            i = i.replace('#', '')
            print(i, end='')


if __name__ == '__main__':
    main()
