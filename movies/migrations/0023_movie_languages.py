# Generated by Django 4.0.5 on 2022-06-17 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0016_spokenlanguage_delete_language'),
        ('movies', '0022_alter_movie_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='languages',
            field=models.ManyToManyField(blank=True, to='management.spokenlanguage'),
        ),
    ]