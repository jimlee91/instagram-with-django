# Generated by Django 3.0.4 on 2020-03-14 19:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200314_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator('^010-?[0-9]\\d{4}-?\\d{4}$')]),
        ),
    ]
