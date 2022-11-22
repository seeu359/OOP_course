from oop.part_2.private_public_method_setters_and_getters import \
    rectangle_point as rp


def test_rectangle_point_type():

    rectangle1 = rp.Rectangle(1, 2, 3, 4)
    rectangle2 = rp.Rectangle(rp.Point(1, 2), rp.Point(4, 3))
    assert isinstance(rectangle1.get_coords()[0], rp.Point) and \
           isinstance(rectangle2.get_coords()[1], rp.Point)


def test_setter_in_rectangle():

    rectangle = rp.Rectangle(1, 2, 3, 4)
    rectangle.set_coords(rp.Point(10, 20), rp.Point(40, 30))
    assert rectangle.get_coords()[0].get_coords()[0] == \
           rp.Point(10, 20).get_coords()[0]
    assert rectangle.get_coords()[1].get_coords()[1] == \
           rp.Point(10, 30).get_coords()[1]
