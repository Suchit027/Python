def gcd(lis):
    maxi = max(lis)
    for i in range(maxi, 0, -1):
        check = 1
        for j in lis:
            if j % i != 0:
                check = 0
                break
        if check == 1:
            print(f'gcd is = {i}')
            break


def main():
    lis = input('enter the list\n')
    lisn = []
    for i in lis:
        lisn.append(int(i))
    gcd(lisn)


if __name__ == '__main__':
    main()
