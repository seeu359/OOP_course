import pytest

from oop.part_1.class_and_static_methods import factory, form_login


def test_factory():

    test_obj = factory.Factory

    assert test_obj.build_number('2') == 2
    assert test_obj.build_sequence() == list()


@pytest.mark.parametrize('name',
                         [('al'),
                          ('test_notvalid_name+'),
                          ])
def test_raise_textinput(name):
    with pytest.raises(ValueError):
        form_login.TextInput(name)


@pytest.mark.parametrize('name',
                         [('a'),
                          ('not-correct.name')
                          ])
def test_raise_passwordinput(name):
    with pytest.raises(ValueError):
        form_login.PasswordInput(name)


def test_textinput():
    test_obj = form_login.TextInput('Alexey', size=13)
    assert test_obj.name == 'Alexey'
    assert test_obj.size == 13


def test_password_input():
    test_object = form_login.PasswordInput('Tirion')
    assert test_object.name == 'Tirion'
    assert test_object.size == 10
