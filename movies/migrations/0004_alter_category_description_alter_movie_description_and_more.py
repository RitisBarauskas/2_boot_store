# Generated by Django 4.2.6 on 2023-10-30 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_category_options_alter_movie_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=980, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=980, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2025)], verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=150, unique=True, verbose_name='Email адрес'),
        ),
    ]
