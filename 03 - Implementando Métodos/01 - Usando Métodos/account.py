class Account:
    def __init__(self, number, holder, balance, limit):
        print("Initializing object... {}".format(self))

        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    # To access the method, just call the object followed by the "." and the method name
    # At the time the function is called, the "self" is filled with the object before the "."
    def extract(self):
        print("{} balance: {}".format(self.holder, self.balance))

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value
