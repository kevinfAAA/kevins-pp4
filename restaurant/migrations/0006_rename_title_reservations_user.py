# Generated by Django 4.0 on 2021-12-13 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_reservations_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservations',
            old_name='title',
            new_name='user',
        ),
    ]