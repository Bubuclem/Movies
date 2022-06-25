# Generated by Django 4.0.5 on 2022-06-25 18:43

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
            name='RequestApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('enable', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date published')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Request API',
                'verbose_name_plural': 'Requests API',
            },
        ),
    ]
