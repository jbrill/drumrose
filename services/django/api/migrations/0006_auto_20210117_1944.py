# Generated by Django 3.1.1 on 2021-01-17 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0005_auto_20200921_1454")]

    operations = [
        migrations.AlterField(
            model_name="playlist",
            name="caption",
            field=models.CharField(blank=True, max_length=200, null=True),
        )
    ]
