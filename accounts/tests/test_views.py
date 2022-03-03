from django.contrib.auth import login
from django import urls
import pytest
from django.urls import reverse 
from accounts.models import CustomUser
import time
from django.contrib.auth import authenticate



@pytest.mark.django_db
def test_login_view(client, new_user1):
    assert CustomUser.objects.count() == 1  #check if the user is created
    client.force_login(new_user1)
    response = client.get(reverse('posts:home')) #check if the user is logged in
    assert response.status_code == 200
    


