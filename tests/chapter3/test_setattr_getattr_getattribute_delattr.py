import pytest
from oop.part_3.setattr_getattr_getattribute_delattr import book


@pytest.mark.parametrize('title, author, pages, year, exp_title, exp_pages',
                         [
                             ('mybook', 'author', 359, 2022, 'mybook', 359),
                             ('mybook2', 'newauthor', 145, 2020, 'mybook2',
                              145),
                         ]
                         )
def test_positive_data_for_book(title, author, pages, year, exp_title, exp_pages):
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
