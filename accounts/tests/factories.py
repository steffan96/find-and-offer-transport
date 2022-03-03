import factory
from faker import Faker
fake = Faker()
from accounts.models import CustomUser


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser
    email = 'test@test.com'
    password = 'secret123'
    first_name = 'testFirstName'
    last_name = 'testLastName'
    city = 'Tokio'
    slug = 'asdasd'
