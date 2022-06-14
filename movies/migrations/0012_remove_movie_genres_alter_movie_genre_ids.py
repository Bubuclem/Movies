# Generated by Django 4.0.4 on 2022-06-08 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_alter_movie_poster_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre_ids',
            field=models.JSONField(blank=True),
        ),
    ]