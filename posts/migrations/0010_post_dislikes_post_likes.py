# Generated by Django 4.0 on 2021-12-24 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_likedislike'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.SmallIntegerField(default=0),
        ),
    ]
