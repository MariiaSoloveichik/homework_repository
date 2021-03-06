"""
You are given the following code:
class Order:
    morning_discount = 0.25
    def __init__(self, price):
        self.price = price
    def final_price(self):
        return self.price - self.price * self.morning_discount
Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy
Example of the result call:
def morning_discount(order):
    ...
def elder_discount(order):
    ...
order_1 = Order(100, morning_discount)
assert order_1.final_price() == 75
order_2 = Order(100, elder_discount)
assert order_2.final_price() == 10
"""
from typing import Callable, Union


class Order:
    """
    Describes the order which contain, price and optional discount program.
    """

    def __init__(self, price: Union[float, int],
                 discount: Union[Callable, None] = None):
        """
        Initialised class instance.
        :param price: order price
        :param discount: discount program
        """
        self.price = price
        self.discount = discount

    def final_price(self):
        """
        Final price from given price of order and discount program.
        :return: total order price
        """
        return self.discount(self.price)


def morning_discount(price: Union[float, int]) -> float:
    """
    Function calculate the price with discount 25%.
    :param price:
    :return: price calculation
    """
    return price * 0.75


def elder_discount(price: Union[float, int]) -> float:
    """
        Function calculate the price with discount 90%.
        :param price:
        :return: price calculation
        """
    return price * 0.1


if __name__ == "__main__":
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 75
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
