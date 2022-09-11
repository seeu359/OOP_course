import pytest

from oop.part_1.classes_and_objects import figure, person


@pytest.fixture()
def figure_fixture():
    setattr(figure.fig1, 'color', 'green')
    delattr(figure.fig1, 'start_pt')


@pytest.fixture()
def person_fixture():
    if 'job' in person.p1.__dict__:
        return True
    else:
        return False
