class Product:
    def __init__(self, name, price=0.0, quantity=0):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def buy(self):
        self.__quantity -= 1

    def product(self):
        print("{}-> Price: {}, Quantity: {}".format(self.__name, self.__price, self.__quantity))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @staticmethod
    def increase_price(product):
        product.__price *= 1.1
