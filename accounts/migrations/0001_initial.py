# Generated by Django 4.0 on 2022-04-15 21:35

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={
                            "unique": "Korisnik sa ovom email adresom već postoji."
                        },
                        max_length=70,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z]*$", "Only letters are allowed."
                            )
                        ],
                        verbose_name="email",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=40,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z]*$", "Only letters are allowed."
                            )
                        ],
                        verbose_name="first_name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=40,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z]*$", "Only letters are allowed."
                            )
                        ],
                        verbose_name="last_name",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        max_length=60,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z]*$", "Only letters are allowed."
                            )
                        ],
                        verbose_name="city",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="joined"),
                ),
                (
                    "last_seen",
                    models.DateTimeField(auto_now=True, verbose_name="last_seen"),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "image",
                    models.ImageField(default="default.jpg", upload_to="profile_pics"),
                ),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="Slug"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
