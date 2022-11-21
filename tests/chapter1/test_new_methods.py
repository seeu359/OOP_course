import pytest
import oop.part_1.new_method.dialog
from oop.part_1.new_method import singleton_five as sf
from oop.part_1.new_method.dialog import Dialog, DialogLinux, DialogWindows
from oop.part_1.new_method.point import Point
from oop.part_1.new_method import factory


def test_singleton_five():
    sf_objects = [sf.SingletonFive(str(n)) for n in range(7)]
    sixth_obj = sf_objects[5]
    fifth_obj = sf_objects[4]
    assert sixth_obj == fifth_obj


@pytest.mark.parametrize('type_os, _name, expected_type',
                         [(3, 'first_name', DialogLinux),
                          (1, 'second_name', DialogWindows)]
                         )
def test_dialog(type_os, _name, expected_type, mocker):
    mocker.patch.object(oop.part_1.new_method.dialog, 'TYPE_OS', type_os)
    test_obj = Dialog(_name)
    assert isinstance(test_obj, expected_type)
    assert test_obj.name == _name


def test_point():
    test_obj1 = Point(1, 2)
    test_obj2 = Point(1, 2).clone()
    assert test_obj1.x == test_obj2.x
    assert test_obj1.y == test_obj2.y


def test_factory():
    assert factory.Factory().build_sequence() == list()
    assert isinstance(factory.Factory().build_number('5'), float)


def test_loader():
    test_obj = factory.Loader()
    test_data = '1, 43, 222'
    result = test_obj.parse_format(test_data, factory.Factory())
    assert result == [1.0, 43.0, 222.0]

