# Generated by Django 2.1.2 on 2018-11-09 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_song_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Post'),
        ),
    ]