from oop.part_2.descriptors import float_value as fv


def test_float_value():
    table = fv.TableSheet(5, 3)
    last_item = table.cells[4][-1]
    first_item = table.cells[0][0]
    assert len(table.cells) == 5
    assert last_item.value == 0.0
    assert first_item.value == 0.0


def test_fill_out_cells():
    table = fv.TableSheet(5, 4)
    table.cells = [[fv.Cell(float(i + 1 + j * table.M))
                    for i in range(table.M)]
                   for j in range(table.N)]
    assert table.cells[0][0].value == 1.0
    assert table.cells[4][3].value == 20.0
