# Generated by Django 2.1.2 on 2018-10-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_album_artists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='albums',
            field=models.ManyToManyField(blank=True, to='api.Album'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='songs',
            field=models.ManyToManyField(blank=True, to='api.Song'),
        ),
    ]