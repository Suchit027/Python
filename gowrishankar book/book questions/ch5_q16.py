def btod(bnum):
    length = len(bnum)
    ans = 0
    bnum = list(bnum)
    bnum.reverse()
    for i in range(0, length):
        ans += int(bnum[i]) * (2 ** i)
    return ans


def main():
    bnum = input('enter binary number\n')
    print(f'decimal number is {btod(bnum)}')


if __name__ == '__main__':
    main()
