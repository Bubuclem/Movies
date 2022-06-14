# Generated by Django 4.0.5 on 2022-06-10 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0003_alter_actor_gender'),
        ('management', '0007_cast_crew_credit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cast',
        ),
        migrations.AlterField(
            model_name='credit',
            name='cast',
            field=models.ManyToManyField(to='actors.actor'),
        ),
    ]