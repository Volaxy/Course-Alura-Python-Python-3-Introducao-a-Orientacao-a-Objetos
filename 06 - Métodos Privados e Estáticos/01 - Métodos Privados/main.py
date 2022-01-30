from account import Account
from client import Client


def main():
    account = Account(1, "Gustavo", 100, 500)
    print(account.limit)

    account.withdraw(1000)


if __name__ == "__main__":
    main()
