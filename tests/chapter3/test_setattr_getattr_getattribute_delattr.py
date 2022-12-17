import pytest
from loguru import logger
from oop.part_3.setattr_getattr_getattribute_delattr import book, shop, \
    course, museum, smartphone, circle, geyser_classic


@pytest.mark.parametrize('title, author, pages, year, exp_title, exp_pages',
                         [
                             ('mybook', 'author', 359, 2022, 'mybook', 359),
                             ('mybook2', 'newauthor', 145, 2020, 'mybook2',
                              145),
                         ]
                         )
def test_positive_data_for_book(title, author, pages, year, exp_title,
                                exp_pages):
    _book = book.Book(title, author, pages, year)
    assert _book.title == exp_title
    assert _book.pages == exp_pages


@pytest.mark.parametrize('title, author, pages, year',
                         [
                             ('true title', 'true author', '232', 20),
                             (22, 'another author', 222, 2022),
                         ]
                         )
def test_negative_data_for_book(title, author, pages, year):
    with pytest.raises(TypeError):
        book.Book(title, author, pages, year)


def test_shop_add_and_delete_goods():
    _shop = shop.Shop('Some name')
    product1 = shop.Product('orange', 100, 150)
    product2 = shop.Product('apple', 150, 100)
    _shop.add_product(product1)
    _shop.add_product(product2)
    assert len(_shop.goods) == 2
    _shop.remove_product(product1)
    assert len(_shop.goods) == 1
    assert product1 not in _shop.goods
    assert product2 in _shop.goods


@pytest.mark.parametrize('name, weight, price, error',
                         [('apple', '100', 150, TypeError),
                          ('apple', 100.12, '150', TypeError),
                          ]
                         )
def test_product_with_raises_type_error(name, weight, price, error):
    with pytest.raises(error):
        shop.Product(name, weight, price)


def test_product_with_raises_attribute_error():
    with pytest.raises(AttributeError):
        _shop = shop.Product('name', 100, 500)
        del _shop.id


@pytest.mark.parametrize('name, practices, duration',
                         [
                             ('hello', '1', 2),
                             (123, 2, 4),
                             ('true name', 40, '15'),
                          ]
                         )
def test_lesson_item(name, practices, duration):
    with pytest.raises(TypeError):
        course.LessonItem(name, practices, duration)


def test_delete_item_from_lesson_and_call_attr_which_not_exist():
    lesson = course.LessonItem('name', 1, 2)
    no_exist_item = lesson.not_exist
    del lesson.title
    del lesson.duration
    del lesson.practices
    assert hasattr(lesson, 'title') and hasattr(lesson, 'duration') and \
           hasattr(lesson, 'practices')
    assert no_exist_item is False


def test_museum():
    _museum = museum.Museum('New museum')
    picture = museum.Picture('New picture', 'author', 'some description')
    mummies = museum.Mummies('Mummi', 'Egypt', 'some descr')
    papyri = museum.Papyri('Papyri', '1900', 'some descr')
    _museum.add_exhibit(papyri)
    _museum.add_exhibit(picture)
    _museum.add_exhibit(mummies)
    assert len(_museum.exhibits) == 3
    _museum.remove_exhibit(mummies)
    assert mummies not in _museum.exhibits


def test_smartphone(test_data_for_smartphone):
    _smartphone = test_data_for_smartphone
    assert len(_smartphone.apps) == 3
    new_yt_app = smartphone.AppYouTube(1204)
    _smartphone.add_app(new_yt_app)
    logger.info(_smartphone.apps)
    assert len(_smartphone.apps) == 3
    assert new_yt_app not in _smartphone.apps


def test_circle():
    _circle = circle.Circle(1, 2, 5)
    _circle.radius = -2
    _circle.x = 5
    _circle.y = 3
    assert _circle.radius == 5
    assert _circle.x == 5
    assert _circle.y == 3


@pytest.mark.parametrize('x, y, radius',
                         [
                             ('1', 2, 10),
                             (2, '4', 5),
                             (3, 5, '7'),
                         ])
def test_circle_with_raises(x, y, radius):
    with pytest.raises(TypeError):
        circle.Circle(x, y, radius)


def test_filter_method(test_data_for_geiser):
    geiser = geyser_classic.GeyserClassic()
    geiser.add_filter(3, test_data_for_geiser['calc'])
    geiser.add_filter(2, test_data_for_geiser['aragon'])
    geiser.add_filter(1, test_data_for_geiser['mech'])
    assert len(geiser.get_filters()) == 3
    assert geiser.water_on() is True
    geiser.remove_filter(2)
    assert geiser.water_on() is False
