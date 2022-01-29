from account import Account


def main():
    acc1 = Account(1, "Gustavo", 500, 1000)
    acc2 = Account(2, "Gabriella", 700, 1500)
    acc1.extract()
    acc2.extract()

    acc1.transfer(acc2, 50)
    acc1.extract()
    acc2.extract()


if __name__ == "__main__":
    main()
