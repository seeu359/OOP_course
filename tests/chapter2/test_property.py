from random import choice
from string import ascii_letters
from oop.part_2.propetry.car import Car
from oop.part_2.propetry.window_dlg import WindowDlg
from oop.part_2.propetry.radius_vector import RadiusVector2D
from oop.part_2.propetry import stack_object as so
from oop.part_2.propetry import tree_obj
from oop.part_2.propetry.path_lines import LineTo, PathLines


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


def test_stack():
    s = so.Stack()
    top = so.StackObj("obj_1")
    s.push(top)
    s.push(so.StackObj("obj_2"))
    s.push(so.StackObj("obj_3"))
    s.pop()

    res = s.get_data()
    assert res == ["obj_1",
                   "obj_2"]
    assert s.top == top


def test_data_which_return_pop_method():
    s = so.Stack()
    top = so.StackObj("name_1")
    s.push(top)
    obj = s.pop()
    assert obj == top


def test_stack_which_return_empty_list():
    s = so.Stack()
    top = so.StackObj("obj_1")
    s.push(top)
    s.pop()
    assert s.get_data() == []


def test_tree_obj1(test_data_for_tree_obj):
    root = test_data_for_tree_obj
    assert tree_obj.DecisionTree.predict(root, [1, 1, 0]) == 'test1'


def test_path_lines():
    path_line = PathLines(LineTo(2, 1), PathLines(3, 1))
    assert len(path_line.points) == 3
    path_line.add_line(LineTo(5, 10))
    last_obj = path_line.points[-1]
    assert len(path_line.get_path()) == 4
    assert last_obj.y == 10
    assert last_obj.x == 5


def test_path_line_main_logic():
    p = PathLines(LineTo(1, 2))
    assert round(p.get_length(), 2) == 2.24
    p.add_line(LineTo(10, 20))
    p.add_line(LineTo(5, 17))
    assert round(p.get_length(), 2) == 28.19
