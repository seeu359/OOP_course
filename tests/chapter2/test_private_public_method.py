from oop.part_2.private_public_method_setters_and_getters.clock import Clock
from oop.part_2.private_public_method_setters_and_getters import linked_list \
    as ll


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


def test_linked_list(object_lists):
    linked_list = ll.LinkedList()
    linked_list.add_obj(object_lists[1])
    linked_list.add_obj(object_lists[2])
    linked_list.add_obj(object_lists[3])
    assert linked_list.tail.get_prev().get_data() == \
           object_lists.get(2).get_data()
    assert linked_list.head.get_next().get_data() == \
           object_lists.get(2).get_data()
    assert linked_list.get_data() == ['data1', 'data2', 'data3']


def test_linked_list_removed(object_lists):
    linked_list = ll.LinkedList()
    linked_list.add_obj(object_lists[1])
    linked_list.add_obj(object_lists[2])
    linked_list.add_obj(object_lists[3])
    linked_list.remove_obj()
    linked_list.remove_obj()
    assert linked_list.head is linked_list.tail
    assert linked_list.tail.get_next() is None
    assert linked_list.head.get_next() is None
    assert linked_list.tail.get_prev() is None
    assert linked_list.head.get_prev() is None
    assert linked_list.get_data() == ['data1']
