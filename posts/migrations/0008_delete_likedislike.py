# Generated by Django 4.0 on 2021-12-24 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_body_likedislike'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LikeDislike',
        ),
    ]