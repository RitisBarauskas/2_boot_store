# Generated by Django 4.2.6 on 2023-11-02 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_category_description_alter_movie_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='category',
            new_name='categories',
        ),
    ]
