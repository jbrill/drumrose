# Generated by Django 2.1.2 on 2018-11-25 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neptuneapi', '0009_neptunesong_apple_music_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neptunesong',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='neptunesong',
            name='artist',
        ),
    ]