import re


def validity(sen):
    pal = re.compile(r'[a-z]')
    pau = re.compile(r'[A-Z]')
    pad = re.compile(r'\d')
    pas = re.compile(r'[$#@]')
    if 6 <= len(sen) <= 12:
        if not pal.search(sen):
            print('no lower case letter')
            return
        if not pau.search(sen):
            print('no upper case letter')
            return
        if not pad.search(sen):
            print('no digit')
            return
        if not pas.search(sen):
            print('no symbol')
            return
    else:
        print('length not in range')
        return
    print('valid')
    return


def main():
    sen = input('enter password ')
    validity(sen)


if __name__ == '__main__':
    main()
