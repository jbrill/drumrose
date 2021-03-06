# Generated by Django 3.2.7 on 2022-02-03 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("api", "0010_auto_20220203_1623")]

    operations = [
        migrations.RenameField(
            model_name="followcontain",
            old_name="follower_user_id",
            new_name="follower_user",
        ),
        migrations.RenameField(
            model_name="followcontain",
            old_name="following_user_id",
            new_name="following_user",
        ),
        migrations.AlterUniqueTogether(
            name="followcontain", unique_together={("follower_user", "following_user")}
        ),
    ]
