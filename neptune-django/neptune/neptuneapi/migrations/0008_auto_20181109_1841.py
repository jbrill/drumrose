# Generated by Django 2.1.2 on 2018-11-09 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neptuneapi', '0007_auto_20181109_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neptuneuser',
            name='handle',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
