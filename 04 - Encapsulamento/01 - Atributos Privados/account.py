class Account:
    def __init__(self, number, holder, balance, limit):
        print("Initializing object... {}".format(self))

        # To restrict the access to the attributes, un "__" is placed before the attribute name, to represents that it
        # is a private attribute
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    # Functions
    def extract(self):
        print("{} balance: {}".format(self.__holder, self.__balance))

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value
