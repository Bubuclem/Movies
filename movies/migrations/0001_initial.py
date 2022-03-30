# Generated by Django 4.0.1 on 2022-03-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('poster_path', models.CharField(max_length=50)),
                ('overview', models.TextField()),
                ('release_date', models.DateField()),
                ('original_title', models.CharField(max_length=50)),
                ('original_language', models.CharField(max_length=2)),
                ('backdrop_path', models.CharField(max_length=50)),
                ('popularity', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('adult', models.BooleanField()),
            ],
        ),
    ]
