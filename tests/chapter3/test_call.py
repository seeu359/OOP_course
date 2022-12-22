import pytest
from oop.part_3.call_method import image_file_acceptor as ia


def test_random_pass(test_data_for_randon_pass):
    a = test_data_for_randon_pass()
    assert isinstance(a, str)
    assert test_data_for_randon_pass.min_length \
           <= len(a) <= \
           test_data_for_randon_pass.max_length


@pytest.mark.parametrize('file_list, expected',
                         [
                             (["boat.jpg", "web.png", "text.txt",
                              "python.doc", "ava.8.jpg",
                               "forest.jpeg", "eq_1.png", "eq_2.png",
                               "my.html", "data.shtml"], 5),
                             (['some.png', 'another.format', 'anotheryet.png',
                              'photo.jpg', 'mus.mp4', 'image.jpg'], 4)
                         ])
def test_image_acceptor(file_list, expected):
    obj = ia.ImageFileAcceptor(('jpg', 'png'))
    file_list = list(filter(obj, file_list))
    assert len(file_list) == expected
