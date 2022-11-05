import pytest
import oop.part_1.new_method.dialog
from oop.part_1.new_method import singleton_five as sf
from oop.part_1.new_method.dialog import Dialog, DialogLinux, DialogWindows


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
