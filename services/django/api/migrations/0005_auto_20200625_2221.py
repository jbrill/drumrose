# Generated by Django 2.1.2 on 2020-06-25 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_auth0managementtoken"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auth0managementtoken",
            name="access_token",
            field=models.SlugField(blank=True, max_length=500, null=True),
        ),
    ]