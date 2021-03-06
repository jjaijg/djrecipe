# Generated by Django 3.0.5 on 2020-05-07 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20200506_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='description',
            new_name='cuisine',
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_hours',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='recipe',
            name='time_min',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(0)]),
        ),
    ]
