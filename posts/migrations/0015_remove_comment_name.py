# Generated by Django 4.0 on 2021-12-25 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
