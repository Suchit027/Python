import re


def main():
    pattern = re.compile(r'(\w+)\s\d{3}-\d{8}')
    with open('P_10.1.txt', 'r') as file:
        print('starting')
        for each in file:
            match_object = pattern.search(each)
            if match_object:
                print(match_object.group(1))


if __name__ == '__main__':
    main()
