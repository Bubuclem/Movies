# Generated by Django 4.0.4 on 2022-06-08 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='backdrop_path',
            field=models.TextField(blank=True, null=True),
        ),
    ]