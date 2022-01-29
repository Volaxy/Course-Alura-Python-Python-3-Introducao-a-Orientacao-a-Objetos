from account import Account


def main():
    acc1 = Account(1, "Gustavo", 500, 1000)
    acc1.extract()

    # Even if the attribute becomes private, the access to it is still possible through "_Account__balance"
    acc1._Account__balance = 1000
    acc1.extract()


if __name__ == "__main__":
    main()
