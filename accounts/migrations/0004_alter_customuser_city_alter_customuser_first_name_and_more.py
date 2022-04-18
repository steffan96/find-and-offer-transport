# Generated by Django 4.0 on 2022-04-15 21:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(max_length=60, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Dozvoljena su samo slova.')], verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Dozvoljena su samo slova.')], verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Dozvoljena su samo slova.')], verbose_name='last_name'),
        ),
    ]