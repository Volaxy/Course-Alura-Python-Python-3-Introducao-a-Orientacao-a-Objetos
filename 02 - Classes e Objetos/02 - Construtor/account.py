class Account:
    # The "__init__" is a constructor of the Class when the code "Account()" is executed
    # To construct an object with defined values, in the time of the constructor call, the values are passed by
    # parameter. Ex.: "account = Account(2, "Valeria", 1000, 10000)"
    def __init__(self, number, holder, balance, limit):
        # The "self" is the value of the object reference
        print("Initializing object... {}".format(self))

        # To create Attributes of the Object, after the "self", we put the "." and then the name of attribute
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit
