class BankAccount:
    def __init__(self, name):
        self.user_name = name
        self.balance = 0.

    def showBalance(self):
        print(f'{self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('insufficient balance')
            return 0
        else:
            self.balance -= amount
            return amount

    def deposit(self, amount):
        self.balance += amount
        return


def main():
    ob1 = BankAccount('test')
    ob1.deposit(1000)
    ob1.showBalance()
    ob1.withdraw(2000)
    ob1.showBalance()


if __name__ == '__main__':
    main()
