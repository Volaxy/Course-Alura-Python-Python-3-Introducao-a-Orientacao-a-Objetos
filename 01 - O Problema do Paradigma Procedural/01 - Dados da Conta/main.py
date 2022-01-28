"""
To represents a great group of data, it's not a good idea instantiate several variables, The great idea is to create
Objects
"""


def create_account(number, holder, balance, limit):
    account = {"number": number, "holder": holder, "balance": balance, "limit": limit}

    return account
