class default:
    def __init__(self, test1=1, test2=2):
        self.test1 = test1
        self.test2 = test2
        self.test = "hello"

    def display(self):
        print(self.test1 + self.test2)
        print(self.test)

test = default(3)
test.display()
