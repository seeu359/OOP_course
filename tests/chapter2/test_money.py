import pytest
from oop.part_2.private_public_method_setters_and_getters.money import Money


@pytest.mark.parametrize('value, expected',
                         [(-5, 20),
                          (40, 40),
                          (0, 0),
                         ])
def test_invalid_money_value(value, expected):

    money = Money(20)
    money.set_money(value)
    assert money.get_money() == expected


def test_add_money():
    money1 = Money(40)
    money2 = Money(60)
    money1.add_money(money2)
    assert money1.get_money() == 100
