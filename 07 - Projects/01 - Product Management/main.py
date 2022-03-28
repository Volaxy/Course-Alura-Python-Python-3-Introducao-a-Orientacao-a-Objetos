from product import Product


def __main__():
    p1 = Product("Rice", 15.0, 5)
    print(type(p1))
    print(p1)
    p1.product()

    p1.buy()
    p1.buy()

    p1.name = "Sugar"
    p1.product()

    Product.increase_price(p1)
    p1.product()


if __name__ == "__main__":
    __main__()
