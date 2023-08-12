def count(sen):
    dic = dict(digit=0, upper=0, lower=0)
    for i in sen:
        if i.isdigit():
            dic["digit"] += 1
        if i.isupper():
            dic["upper"] += 1
        if i.islower():
            dic["lower"] += 1
    return dic


def main():
    print('enter sentence')
    sen = input()
    print(count(sen))


if __name__ == '__main__':
    main()
