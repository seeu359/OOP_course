from oop.part_2.private_public_method_setters_and_getters import line


def test_line():
    _line = line.Line(1, 2, 3, 4)
    _line.set_coords(2, 3, 5, 7)
    assert _line.get_coords()[0] == 2
    assert _line.get_coords()[3] == 7
    assert isinstance(_line.get_coords(), tuple)
