import pytest
from oop.part_2.propetry import tree_obj
from oop.part_1.classes_and_objects import figure, person
from oop.part_1.class_methods import graph, translator
from oop.part_1.initializer_init import cpu
from oop.part_2.private_public_method_setters_and_getters.linked_list\
    import ObjList

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


@pytest.fixture()
def cpu_fixture():
    my_cpu = cpu.CPU('RYZEN', 2.2)
    memory = cpu.Memory('Hyper1', 3000), cpu.Memory('hyper2', 2000)
    return my_cpu, memory


@pytest.fixture()
def object_lists():
    objects_dict = {
        1: ObjList('data1'),
        2: ObjList('data2'),
        3: ObjList('data3'),
    }
    return objects_dict


@pytest.fixture()
def test_data_for_tree_obj():
    root = tree_obj.DecisionTree.add_obj(tree_obj.TreeObj(0))
    obj1 = tree_obj.DecisionTree.add_obj(tree_obj.TreeObj(1), root)
    obj2 = tree_obj.DecisionTree.add_obj(tree_obj.TreeObj(2), root, False)
    tree_obj.DecisionTree.add_obj(tree_obj.TreeObj(-1, 'test1'), obj1)
    tree_obj.DecisionTree.add_obj(tree_obj.TreeObj(-1, 'test2'), obj1, False)
    tree_obj.DecisionTree.add_obj(
        tree_obj.TreeObj(-1, "test3"), obj2
    )
    tree_obj.DecisionTree.add_obj(tree_obj.TreeObj(-1, "test4"), obj2, False)
    return root