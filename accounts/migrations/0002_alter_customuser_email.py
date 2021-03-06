# Generated by Django 4.0 on 2022-04-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(
                error_messages={
                    "unique": "Korisnik sa ovom email adresom već postoji."
                },
                max_length=70,
                unique=True,
                verbose_name="email",
            ),
        ),
    ]
