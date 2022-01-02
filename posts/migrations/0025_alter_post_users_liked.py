# Generated by Django 4.0 on 2022-01-02 16:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0024_post_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='users_liked',
            field=models.ManyToManyField(blank=True, null=True, related_name='users_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
