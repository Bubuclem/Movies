# Generated by Django 4.0.1 on 2022-03-31 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_poster_path_alter_show_poster_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='backdrop_path',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='backdrop_path',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
