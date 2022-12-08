import pytest
from oop.part_2.descriptors import bag
from oop.part_2.descriptors import super_shop as sp
from oop.part_2.descriptors import float_value as fv
from oop.part_2.descriptors import validate_form as vf


def test_float_value():
    table = fv.TableSheet(5, 3)
    last_item = table.cells[4][-1]
    first_item = table.cells[0][0]
    assert len(table.cells) == 5
    assert last_item.value == 0.0
    assert first_item.value == 0.0


def test_fill_out_cells():
    table = fv.TableSheet(5, 4)
    table.cells = [[fv.Cell(float(i + 1 + j * table.M))
                    for i in range(table.M)]
                   for j in range(table.N)]
    assert table.cells[0][0].value == 1.0
    assert table.cells[4][3].value == 20.0


def test_validate_form():
    form = vf.RegisterForm('login', 'password', 'email@test.com')
    assert len(form.get_fields()) == 3
    assert form.login == 'login'
    form.login = 'a'
    assert form.login == 'login'


@pytest.mark.parametrize('_min, _max, value, expected',
                         [
                             (5, 10, 'test', False),
                             (5, 10, 'Test is False', False),
                             (3, 6, 'wow', True),
                             (4, 7, 'ItsTrue', True),
                         ]
                         )
def test_validate_date_from_validate_form(_min, _max, value, expected):
    validator = vf.ValidateString(
        min_length=_min,
        max_length=_max,
    )
    assert validator.validate(value) is expected


def test_super_shop():
    shop = sp.SuperShop('New shop')
    assert shop.name == 'New shop'
    assert isinstance(shop.goods, list)


def test_add_product_in_shop():
    shop = sp.SuperShop('Another shop')
    shop.add_product(sp.Product('First good', 1000))
    shop.add_product(sp.Product('Second good', 2000))
    assert len(shop.goods) == 2
    assert all([isinstance(good, sp.Product) for good in shop.goods]) 


def test_create_product():
    product = sp.Product('Nice goods', 2000)
    product2 = sp.Product('So expensive goods', 20_000)
    assert product.name == 'Nice goods' and product.price == 2000
    assert product2.name == 'So expensive goods'
    assert hasattr(product2, '_price') is False


def test_bag():
    _bag = bag.Bag(100)
    thing1 = bag.Thing('thing1', 50)
    thing2 = bag.Thing('thing2', 20) 
    thing3 = bag.Thing('thing3', 40)
    _bag.add_thing(thing1)
    _bag.add_thing(thing2)
    _bag.add_thing(thing3)
    assert len(_bag.things) == 2
