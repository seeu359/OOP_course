import pytest

from oop.part_1.classes_and_objects import car, goods, database, notes, \
    dictionary, travel_blog, figure, person


@pytest.mark.parametrize('input_value, expected',
                         [(database.DataBase.pk, 1),
                          (database.DataBase.title, 'Классы и объекты'),
                          (database.DataBase.author, 'Сергей Балакирев'),
                          (database.DataBase.views, 14356),
                          (database.DataBase.comments, 12)]
                         )
def test_database(input_value, expected):
    assert input_value == expected


@pytest.mark.parametrize('input_value, expected',
                         [(goods.Goods.weight, 154),
                          (goods.Goods.price, 2048),
                          (goods.Goods.inflation, 100)]
                         )
def test_goods(input_value, expected):
    assert input_value == expected


@pytest.mark.parametrize('input_value, expected',
                         [(car.Car.model, 'Тойота'),
                          (car.Car.color, 'Розовый')]
                         )
def test_car(input_value, expected):
    assert input_value == expected


@pytest.mark.parametrize('input_value, expected',
                         [('uid', 1005435),
                          ('pages', 2)]
                         )
def test_notes(input_value, expected):
    assert getattr(notes.Notes, input_value) == expected


@pytest.mark.parametrize('input_value, default_bool_value, expected',
                         [('eng', False, 'Python'),
                          ('rus_word', False, False)]
                         )
def test_dictionary(input_value, default_bool_value, expected):
    assert getattr(dictionary.Dictionary, input_value,
                   default_bool_value) == expected


def test_travel_blog():
    total_blogs = travel_blog.TravelBlog.total_blogs
    total_blogs += 1
    travel_blog.tb2.days += 1
    assert travel_blog.tb1.name == 'Франция'
    assert total_blogs == 3
    assert travel_blog.tb2.days == 6


@pytest.mark.parametrize('input_value, expected',
                         [(figure.fig1.start_pt, (10, 5)),
                          (figure.fig1.color, 'red')]
                         )
def test_figure(input_value, expected):
    assert input_value == expected


def test_figure2(figure_fixture):
    assert hasattr(figure.fig1, 'start_pt') is False
    assert figure.fig1.color == 'green'


def test_person(person_fixture):
    assert getattr(figure.Figure, 'job', 'Программист')
    assert person_fixture is False
