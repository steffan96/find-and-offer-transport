import time

import pytest
from django import urls
from django.contrib.auth import authenticate, login
from django.urls import reverse

from accounts.models import CustomUser


@pytest.mark.django_db
def test_login_view(client, new_user1):
    assert CustomUser.objects.count() == 1  # check if the user is created
    client.force_login(new_user1)
    response = client.get(reverse("posts:home"))  # check if the user is logged in
    assert response.status_code == 200
