from account import Account
from client import Client


def main():
    # The attribute is replaced or catch by the getter and setter method
    client = Client("marks")
    client.name = "john"
    print(client.name)

    account = Account(1, "Gustavo", 100, 500)
    print(account.limit)
    account.limit = 600
    print(account.limit)


if __name__ == "__main__":
    main()
