from urllib import response

from django.test import TestCase
from django.urls import reverse

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class TestUser(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            email="test@test.com",
            first_name="firstName",
            last_name="lastName",
            is_staff="True",
            slug="asdasd",
        )
        self.user.set_password("secret123")
        self.user.save()
        self.client.login(email="test@test.com", password="secret123")

    def test_update_user_view(self):
        response = self.client.post(
            reverse("accounts:my_profile", kwargs={"slug": "asdasd"}),
            {
                "first_name": "first",
                "last_name": "last",
                "email": "asd@asd.com",
                "city": "Tokio",
            },
        )
        self.assertRedirects(
            response,
            "/posts/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_signup_view(self, request):
        credentials = {
            "email": "test1@test.com",
            "first_name": "test1",
            "last_name": "user1",
            "city": "derventa",
            "password1": "123secret",
            "password2": "123secret",
        }
        self.client.post("http://127.0.0.1:8000/users/logout/")
        response = self.client.post(
            "http://127.0.0.1:8000/users/signup/", credentials, follow=True
        )
        # self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response,
            "/posts/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_update_password_view(self, request):
        credentials = {
            "old_password": "123secret",
            "password1": "321secret",
            "password2": "321secret",
        }
        response = self.client.post(
            "http://127.0.0.1:8000/users/change-password/", credentials, follow=True
        )
        self.assertRedirects(
            response, "/posts/", status_code=302, target_status_code=200
        )
