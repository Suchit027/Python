import math


def sincal(x, n):
    x = (x * math.pi) / 180
    ans = 0
    for i in range(1, n + 1):
        ans += (((-1) ** (i - 1)) * (x ** ((2 * i) - 1))) / math.factorial((2 * i) - 1)
    return ans


def main():
    print('enter x')
    x = int(input())
    print('enter number of terms')
    n = int(input())
    print(sincal(x, n))


if __name__ == '__main__':
    main()
