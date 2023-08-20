print('starting')
try:
    file = open(r"C:\Users\Suchit\Desktop\Python\Python_book\gowrishankar book\Files\File1.txt", 'r+')
    file.write('hello')
    file.close()
    file = open(r"C:\Users\Suchit\Desktop\Python\Python_book\gowrishankar book\Files\File1.txt", 'r+')
    for line in file:
        print(line, end='')
except IOError:
    print('error')
finally:
    file.close()
