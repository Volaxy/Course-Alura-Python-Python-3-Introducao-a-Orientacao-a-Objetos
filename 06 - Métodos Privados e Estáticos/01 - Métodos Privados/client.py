class Client:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        print("Getter Method")
        return self.__name.title()

    @name.setter
    def name(self, name):
        print("Setter Method")
        self.__name = name
