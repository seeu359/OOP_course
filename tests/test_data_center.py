from oop.part_1.class_and_static_methods import data_center as dc


def test_server_ip():
    server1 = dc.Server()
    server2 = dc.Server()
    assert server1.get_ip() == 1
    assert server2.get_ip() == 2


def test_send_data_from_server_to_router():
    router = dc.Router()
    data = dc.Data('test data', 2)
    data2 = dc.Data('test data 2', 2)
    server = dc.Server()
    server.send_data(data)
    server.send_data(data2)
    assert len(router.buffer) == 2
