# Generated by Django 4.0 on 2021-12-21 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(error_messages={'required': 'Popunite ovo polje'}, max_length=200),
        ),
    ]
