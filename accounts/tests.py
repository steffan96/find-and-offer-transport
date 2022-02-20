from urllib import response
from django.test import TestCase
from django.urls import reverse
from .models import CustomUser


class TestUser(TestCase):
    def setUp(self):
        self.credentials = {
            'email': 'test@test.com',
            'password': 'secret123'}
        CustomUser.objects.create(email = 'test@test.com', password = 'secret123',
                                first_name = 'firstName', last_name = 'lastName', 
                                is_staff = 'True', slug = 'asdasd')

    def test_login(self):
        response = self.client.post('http://127.0.0.1:8000/users/login', 
                                        follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/users/login/', 
        status_code=301, 
        target_status_code=200, fetch_redirect_response=True) 

    def test_update_user(self):
        response = self.client.post(reverse('accounts:my_profile', 
        kwargs={'slug': 'asdasd'}), {'first_name': 'first', 'last_name': 'last', 
                                        'email': 'asd@asd.com', 'city': 'Tokio'})
        self.assertEqual(response.status_code, 302)
