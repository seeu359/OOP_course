import pytest

from oop.part_1.classes_and_objects import figure, person
from oop.part_1.class_methods import graph, translator


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


@pytest.fixture()
def graph_fixture():
    test_graph = graph.Graph()
    test_graph.set_data([1, -100, -2, 0, 35, 3, 7, 10])
    test_draw = test_graph.draw()
    return test_draw


@pytest.fixture()
def graph_fixture2():
    test_graph = graph.Graph()
    test_graph.LIMIT_Y = [-10, 20]
    test_graph.set_data([-8, 0, -10, 13, 40, 20, 0, 21, -5, 4])
    test_draw = test_graph.draw()
    return test_draw


@pytest.fixture()
def translator_fixture():
    test_translator_obj = translator.Translator()
    test_translator_obj.add('go', 'ходить')
    test_translator_obj.add('go', 'ехать')
    test_translator_obj.add('swim', 'плавать')
    test_translator_obj.add('swim', 'плавать')
    test_translator_obj.add('go', 'ехать')
    return test_translator_obj
