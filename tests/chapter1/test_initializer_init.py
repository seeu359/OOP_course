import pytest
from oop.part_1.initializer_init import money, point, graph, cpu


@pytest.mark.parametrize('input_value, expected',
                         [('my_money', 100),
                          ('your_money', 10)]
                         )
def test_money(input_value, expected):
    input_value = money.Money(expected)
    assert input_value.money == expected


def test_point():
    assert len(point.points) == 1000
    assert point.points[1].color == 'yellow'


def test_graph():
    test_gr = graph.Graph([2, 3, 4, 6])
    assert isinstance(graph.gr.data, list) is True
    assert graph.gr.data != test_gr.data


@pytest.mark.parametrize('input_value, expected',
                         [(graph.gr.show_table, 'Отображение данных закрыто'),
                          (graph.gr.show_graph, 'Отображение данных закрыто'),
                          (graph.gr.show_bar, 'Отображение данных закрыто')]
                         )
def test_graph2(input_value, expected):
    assert input_value() == expected


def test_cpu(cpu_fixture):
    _cpu, memory = cpu_fixture
    test_mb = cpu.MotherBoard('Asus', _cpu, memory)
    assert isinstance(test_mb.mem_slots, tuple) is True
    assert isinstance(test_mb.cpu, cpu.CPU) is True
    assert len(test_mb.mem_slots) == 2
