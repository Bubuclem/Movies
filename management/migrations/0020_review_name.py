# Generated by Django 4.0.5 on 2022-06-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_alter_review_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
