# Generated by Django 3.1 on 2020-09-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0004_auto_20200920_0305")]

    operations = [
        migrations.RenameField(
            model_name="playlist", old_name="title", new_name="name"
        ),
        migrations.RemoveField(model_name="album", name="page_id"),
        migrations.RemoveField(model_name="playlist", name="page_id"),
        migrations.RemoveField(model_name="song", name="page_id"),
        migrations.AddField(
            model_name="album",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
