from oop.part_1.classes_and_objects import car, goods, database


def test_database():
    assert database.DataBase.pk == 1
    assert database.DataBase.title == 'Классы и объекты'
    assert database.DataBase.author == 'Сергей Балакирев'
    assert database.DataBase.views == 14356
    assert database.DataBase.comments == 12


def test_goods():
    assert goods.Goods.weight == 154
    assert goods.Goods.price == 2048
    assert goods.Goods.inflation == 100


def test_car():
    assert car.Car.model == 'Тойота'
    assert car.Car.color == 'Розовый'
