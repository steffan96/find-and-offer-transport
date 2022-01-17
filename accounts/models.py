import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.db.models.fields import CharField, PositiveBigIntegerField
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth.models import UserManager






class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email', max_length=70, unique=True, 
    error_messages={'unique': 'Korisnik sa ovom email adresom već postoji.'},)
    first_name = models.CharField(verbose_name='first_name', max_length=40)
    last_name = models.CharField(verbose_name='last_name', max_length=40)
    city = models.CharField(verbose_name='city', max_length=60)
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
