from oop.part_2.private_public_method_setters_and_getters.clock import Clock


def test_clock():

    clock = Clock(-1)
    clock2 = Clock(100001)
    clock3 = Clock(20)
    assert clock.get_time() == 0
    assert clock2.get_time() == 0
    assert clock3.get_time() == 20

def test_set_value_for_clock():

    clock = Clock(20)
    clock2 = Clock(30)
    clock.set_time(40)
    clock2.set_time(-1)

    assert clock.get_time() == 40
    assert clock2.get_time() == 30
