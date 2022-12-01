from random import choice
from string import ascii_letters
from oop.part_2.propetry.car import Car
from oop.part_2.propetry.window_dlg import WindowDlg
from oop.part_2.propetry.radius_vector import RadiusVector2D


def test_car():
    car = Car()
    car.model = 'Toyota'
    assert car.model == 'Toyota'
    car.model = 'Lexus'
    assert car.model == 'Lexus'


def test_car_with_error_data():
    car = Car()
    data = ''.join([char for _ in range(120)
                    for char in choice(ascii_letters)])
    car.model = data
    assert car.model is None


def test_window_dlg():
    window = WindowDlg('title', 12, 20)
    window.width = 2.2
    window.height = 10
    assert window.width == 12
    assert window.height == 10
    assert window.show() == 'title: 12, 10'


def test_test_radius_vector():
    rv = RadiusVector2D()
    rv.y = -102
    rv.x = 12.2
    norm = rv.norm2(rv)
    assert rv.y == 0
    assert rv.x == 12.2
    assert round(norm, 2) == 148.84
