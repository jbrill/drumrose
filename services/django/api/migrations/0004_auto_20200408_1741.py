# Generated by Django 2.1.2 on 2020-04-08 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_auto_20200406_1829"),
    ]

    operations = [
        migrations.RemoveField(model_name="song", name="apple_music_id",),
        migrations.AddField(
            model_name="song",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
