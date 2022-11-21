import pytest

from oop.part_1.class_and_static_methods import factory, form_login, \
    card_check, video, viber, appstore


def test_factory():

    test_obj = factory.Factory

    assert test_obj.build_number('2') == 2
    assert test_obj.build_sequence() == list()


@pytest.mark.parametrize('name',
                         [('al'),
                          ('test_notvalid_name+'),
                          ])
def test_raise_textinput(name):
    with pytest.raises(ValueError):
        form_login.TextInput(name)


@pytest.mark.parametrize('name',
                         [('a'),
                          ('not-correct.name')
                          ])
def test_raise_passwordinput(name):
    with pytest.raises(ValueError):
        form_login.PasswordInput(name)


def test_textinput():
    test_obj = form_login.TextInput('Alexey', size=13)
    assert test_obj.name == 'Alexey'
    assert test_obj.size == 13


def test_password_input():
    test_object = form_login.PasswordInput('Tirion')
    assert test_object.name == 'Tirion'
    assert test_object.size == 10


@pytest.mark.parametrize('card, expected',
                         [('0000-1111-2222-3333', True),
                          ('999-3333-2455', False),
                          ('9999-1000-4433-343k', False)]
                         )
def test_card_check(card, expected):
    assert card_check.CardCheck().check_card_number(card) is expected


@pytest.mark.parametrize('name, expected',
                         [('ALEKSEI9 CHEREMUSHKIN', True),
                          ('ALEKS Cheremushkin', False),
                          ('ALEKSEI_CHEREMUSHKIN', False)]
                         )
def test_check_name(name, expected):
    assert card_check.CardCheck().check_name(name) is expected


def test_video():
    new_video = video.Video().create('New video')
    video.YouTube().add_video(new_video)
    assert len(video.YouTube.videos) == 3


def test_app_store():
    app1 = appstore.Application('whatsapp')
    app2 = appstore.Application('vk')
    app3 = appstore.Application('telegram')
    appstore.AppStore().add_application(app1)
    appstore.AppStore().add_application(app2)
    appstore.AppStore().add_application(app3)
    appstore.AppStore().remove_application(app2)
    appstore.AppStore().block_application(app1)
    assert appstore.AppStore().total_apps() == 2
    assert app1.blocked is True


def test_viber():
    msg1 = viber.Message('Hello, world!')
    msg2 = viber.Message('Hello, my friend!')
    msg3 = viber.Message('Hello, Bob!')
    msg4 = viber.Message('Hello, Alex!')
    viber.Viber().add_message(msg1)
    viber.Viber().add_message(msg2)
    viber.Viber().add_message(msg3)
    viber.Viber().add_message(msg4)
    viber.Viber().set_like(msg2)
    viber.Viber().set_like(msg2)
    viber.Viber().remove_message(msg1)
    viber.Viber().set_like(msg4)
    assert viber.Viber().total_messages() == 3
    assert msg2.fl_like is False
    assert msg4.fl_like is True
