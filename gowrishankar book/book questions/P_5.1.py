def palindrome(string):
    nstring = string[::-1]
    if nstring == string:
        return True
    else:
        return False


def main():
    string = input('enter string\n')
    print(f'string is palindrome -  {palindrome(string)}')


if __name__ == '__main__':
    main()
