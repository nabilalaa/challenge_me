# Generated by Django 4.0.5 on 2023-10-02 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenge_me', '0009_rename_player_player_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tournament', to='challenge_me.tournament'),
        ),
    ]