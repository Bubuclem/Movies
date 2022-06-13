# Generated by Django 4.0.5 on 2022-06-13 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0009_alter_show_first_air_date_alter_show_last_air_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.RemoveField(
            model_name='show',
            name='genre_ids',
        ),
        migrations.AddField(
            model_name='show',
            name='genres',
            field=models.ManyToManyField(blank=True, to='shows.genre'),
        ),
    ]
