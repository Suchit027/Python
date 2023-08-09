def word_sort(sen):
    lis = sen.split(' ')
    newlis = list()
    for word in lis:
        newlis.append((len(word), word))
    print(newlis)

def main():
    sen = input('enter ')
    word_sort(sen)

if __name__ == '__main__':
    main()
