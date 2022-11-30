import pytest
from string import ascii_letters, digits
from oop.part_2.private_public_method_setters_and_getters.email_validator \
    import EmailValidator


@pytest.mark.parametrize('email, expected',
                         [
                             ('test@email.ru', True),
                             ('rio0723r2r@gmail.ru', True),
                             ('qwe..@yandex.ru', False),
                             ('hellomail.ru', False),
                             ('jweqfjljlfqw+@maik.com', False),
                             (1111, False)
                         ])
def test_email_validator(email, expected):
    assert EmailValidator.check_email(email) is expected


def test_get_random_email():
    symbols = ascii_letters + digits + '_.'
    r_email = EmailValidator.get_random_email()
    name, _ = r_email.split('@')
    assert len(name) < 100
    assert len(name.strip(symbols)) == 0