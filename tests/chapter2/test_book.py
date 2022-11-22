from oop.part_2.private_public_method_setters_and_getters import book


def test_book():

    _book = book.Book('Bulgakov', 'Master and Margarita', 1000)
    _book.set_price(500)
    _book.set_author('new author')
    _book.set_title('new title')
    assert _book.get_price() == 500
    assert _book.get_author() == 'new author'
    assert _book.get_title() == 'new title'
