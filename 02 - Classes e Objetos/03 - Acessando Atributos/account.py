class Account:
    def __init__(self, number, holder, balance, limit):
        print("Initializing object... {}".format(self))

        # To access the attributes, we type the reference name, and then put the "." followed by the attribute name
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit
