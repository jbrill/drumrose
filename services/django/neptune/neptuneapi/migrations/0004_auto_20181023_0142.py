# Generated by Django 2.1.2 on 2018-10-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neptuneapi', '0003_neptunealbum_artists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neptuneartist',
            name='albums',
            field=models.ManyToManyField(blank=True, to='neptuneapi.NeptuneAlbum'),
        ),
        migrations.AlterField(
            model_name='neptuneartist',
            name='songs',
            field=models.ManyToManyField(blank=True, to='neptuneapi.NeptuneSong'),
        ),
    ]