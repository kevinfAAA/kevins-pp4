# Generated by Django 4.0 on 2021-12-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='number_of_guests',
            field=models.IntegerField(default=1),
        ),
    ]