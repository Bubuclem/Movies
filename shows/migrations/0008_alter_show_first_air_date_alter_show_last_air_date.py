# Generated by Django 4.0.5 on 2022-06-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0007_remove_show_genres_show_homepage_show_in_production_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='first_air_date',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='show',
            name='last_air_date',
            field=models.TextField(blank=True, null=True),
        ),
    ]