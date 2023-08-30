def count(string):
    d = w = u = l = 0
    str = string.split(' ')
    w = len(str)
    for i in string:
        for j in i:
            if j.isdigit():
                d += 1
                continue
            if j.islower():
                l += 1
                continue
            if j.isupper():
                u += 1
    print(f'digits = {d}, words = {w}, upper = {u}, lower = {l}')


def main():
    string = input('enter string\n')
    count(string)


if __name__ == "__main__":
    main()
