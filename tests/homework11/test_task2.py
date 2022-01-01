import pytest

from homework11.task2 import Order, elder_discount, morning_discount


def testing_order_morning_discount():
    """ Testing calculating the price with morning discount """
    order = Order(100, morning_discount)
    assert order.final_price() == 75


def testing_order_elder_discount():
    """ Testing calculating the price with elder discount """
    order = Order(100, elder_discount)
    assert order.final_price() == 90
