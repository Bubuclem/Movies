# Generated by Django 4.0.4 on 2022-06-08 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_remove_movie_genre_ids_movie_genre_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre_ids',
            field=models.TextField(blank=True, null=True),
        ),
    ]