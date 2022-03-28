class Account:
    def __init__(self, number, holder, balance, limit):
        print("Initializing object... {}".format(self))

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

    def transfer(self, origin, value):
        self.__balance += value
        origin.withdraw(value)

    def get_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    def set_limit(self, limit):
        self.__limit = limit
