import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.db.models.fields import CharField, PositiveBigIntegerField
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth.models import UserManager, BaseUserManager


alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Dozvoljena su samo slova.')

# class UserManager(BaseUserManager):
    # def create_user(self, email, password=None, is_admin=False, is_staff=False, is_active=True):
    #     if not email:
    #         raise ValueError("Unesite email adresu.")
    #     if not password:
    #         raise ValueError("Unesite lozinku.")


    #     user = self.model(
    #         email=self.normalize_email(email)
    #     )
    #     user.set_password(password)  # change password to hash
    #     user.admin = is_admin
    #     user.staff = is_staff
    #     user.active = is_active
    #     user.save(using=self._db)
    #     return user
        
    # def create_superuser(self, email, password=None, **extra_fields):
    #     if not email:
    #         raise ValueError("Unesite email adresu.")
    #     if not password:
    #         raise ValueError("Unesite lozinku.")
        
    #     REQUIRED_FIELDS = ['first_name', 'last_name', 'city', 'username']
    #     user = self.model(
    #         email=self.normalize_email(email)
    #     )
    #     user.set_password(password)
    #     user.admin = True
    #     user.staff = True
    #     user.active = True
    #     user.save(using=self._db)
    #     return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length=70, unique=True, 
        error_messages={'unique': 'Korisnik sa ovom email adresom već postoji.'})
    first_name = models.CharField(verbose_name='first_name', max_length=40,
                                                    validators=[alphanumeric])
    last_name = models.CharField(verbose_name='last_name', max_length=40,
                                                    validators=[alphanumeric])
    city = models.CharField(verbose_name='city', max_length=60,
                                                    validators=[alphanumeric])
    date_joined = models.DateTimeField(verbose_name='joined', auto_now_add=True)
    last_seen = models.DateTimeField(verbose_name='last_seen', auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)

    #is_superuser = models.BooleanField(default=False)
    #user_permissions = models.PositiveIntegerField(default=None)

    def save(self, *args, **kwargs):
        if not self.slug:
            random_slug = uuid.uuid4()
            self.slug = slugify(random_slug)
        super(CustomUser, self).save(*args, **kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'city']

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


