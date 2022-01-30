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
        if self.__can_withdraw(value):
            self.__balance -= value
        else:
            print("The value of {} exceeded the limit".format(value))

    # To define a private method, it's placed a "__" before the method name
    def __can_withdraw(self, value):
        return value <= self.__balance + self.__limit

    def transfer(self, origin, value):
        self.__balance += value
        origin.withdraw(value)

    def get_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit
