class default:
    def __init__(self, test1=1, test2=2):
        self.test1 = test1
        self.test2 = test2

    def display(self):
        print(self.test1  + self.test2)


test = default(3)
test.display()
