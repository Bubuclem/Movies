# Generated by Django 4.0.5 on 2022-06-25 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '__first__'),
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
        migrations.CreateModel(
            name='LastEpisode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_date', models.DateField()),
                ('season_number', models.IntegerField()),
                ('episode_number', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('production_code', models.CharField(max_length=255)),
                ('still_path', models.CharField(blank=True, max_length=255, null=True)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('air_date', models.DateField(blank=True, null=True)),
                ('episode_count', models.IntegerField()),
                ('season_number', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('overview', models.TextField(blank=True)),
                ('homepage', models.CharField(blank=True, max_length=255)),
                ('tagline', models.CharField(blank=True, max_length=255)),
                ('type', models.CharField(blank=True, max_length=255)),
                ('first_air_date', models.DateField(blank=True, null=True)),
                ('last_air_date', models.DateField(blank=True, null=True)),
                ('in_production', models.BooleanField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Rumored', 'Rumeur'), ('Planned', 'Planifié'), ('In Production', 'En production'), ('Post Production', 'Post production'), ('Released', 'Sorti'), ('Canceled', 'Annulé'), ('Returning Series', 'Série en cours'), ('Ended', 'Terminé')], max_length=255, null=True)),
                ('popularity', models.FloatField(blank=True)),
                ('vote_count', models.IntegerField(blank=True)),
                ('vote_average', models.FloatField(blank=True)),
                ('number_of_episodes', models.IntegerField(blank=True, null=True)),
                ('number_of_seasons', models.IntegerField(blank=True, null=True)),
                ('poster_path', models.TextField(blank=True, null=True)),
                ('backdrop_path', models.TextField(blank=True, null=True)),
                ('original_language', models.CharField(blank=True, max_length=255)),
                ('original_name', models.CharField(blank=True, max_length=255)),
                ('genres', models.ManyToManyField(blank=True, to='shows.genre')),
                ('languages', models.ManyToManyField(blank=True, to='management.spokenlanguage')),
                ('last_episode', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shows.lastepisode')),
                ('seasons', models.ManyToManyField(blank=True, to='shows.season')),
            ],
        ),
    ]
