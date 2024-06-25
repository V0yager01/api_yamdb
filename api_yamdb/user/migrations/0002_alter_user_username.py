# Generated by Django 3.2 on 2024-06-25 15:22

import django.contrib.auth.validators
from django.db import migrations, models
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator(), user.validators.validate_me]),
        ),
    ]
