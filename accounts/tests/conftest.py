import pytest
from pytest_factoryboy import register

from .factories import UserFactory

register(UserFactory)


@pytest.fixture
def new_user1(db, user_factory):
    user = user_factory.create()
    return user
