from account import Account


def main():
    acc1 = Account(1, "Gustavo", 500, 1000)
    acc1.extract()

    acc1.deposit(15)
    acc1.extract()

    acc1.withdraw(100)
    acc1.extract()


if __name__ == "__main__":
    main()
