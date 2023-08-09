def count(word):
    dic = dict()
    for each_character in word:
        dic[each_character] = dic.get(each_character, 0) + 1
    return dic


def main():
    print('enter word')
    word = input()
    dic = count(word)
    print(dic)


if __name__ == '__main__':
    main()
