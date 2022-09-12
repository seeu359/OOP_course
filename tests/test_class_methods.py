import pytest

from oop.part_1.class_methods import media_player, database


@pytest.mark.parametrize('input_value, object_attr, expected',
                         [(media_player.media1.open('file1'),
                           media_player.media1.filename, 'file1'),
                          (media_player.media2.open('file2'),
                           media_player.media2.play(),
                           'Воспроизведение file2')]
                         )
def test_media_player(input_value, object_attr, expected):
    assert object_attr == expected


def test_graph(graph_fixture, graph_fixture2):
    fixture1_result = '1 0 3 7 10'
    fixture2_result = '-8 0 -10 13 20 0 -5 4'
    assert fixture1_result == graph_fixture
    assert fixture2_result == graph_fixture2


def test_database():
    list_input = ['1 Ivan 46 300000', '2 Alexey 27 270000', '3 John 30 180000']
    _database = database.DataBase()
    _database.insert(list_input)
    result = _database.select(2, 5)
    assert result == [{'id': '3',
                       'name': 'John',
                       'old': '30',
                       'salary': '180000'}]
    assert _database.lst_data[1]['name'] == 'Alexey'
