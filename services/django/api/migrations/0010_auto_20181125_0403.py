# Generated by Django 2.1.2 on 2018-11-25 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_song_apple_music_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
    ]