from account import Account


def main():
    acc1 = Account(1, "Gustavo", 500, 1000)

    print(acc1.get_holder())
    print(acc1.get_balance())
    print(acc1.set_limit(500))


if __name__ == "__main__":
    main()
