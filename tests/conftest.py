import pytest


@pytest.fixture
def user_credentials(django_user_model):
    username = 'test'
    password = 'testpass'
    django_user_model.objects.create_user(username=username, password=password)
    return {'username': username, 'password': password}
