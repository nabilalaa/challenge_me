# Generated by Django 4.0.5 on 2023-10-02 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge_me', '0008_rename_players_player'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='player',
            new_name='name',
        ),
    ]