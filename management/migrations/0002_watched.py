# Generated by Django 4.0.4 on 2022-05-25 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watched',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('media_id', models.IntegerField()),
                ('media_type', models.CharField(choices=[('movie', 'Movie'), ('tv', 'Show')], default='movie', max_length=5)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]