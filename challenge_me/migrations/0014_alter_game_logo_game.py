# Generated by Django 4.2.11 on 2025-06-09 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge_me', '0013_alter_game_logo_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='logo_game',
            field=models.ImageField(blank=True, default='w_1000,ar_1:1,c_fill,g_auto,e_art:hokusai/v1749456146/challenge_z4tlpe.png', null=True, upload_to='challenge'),
        ),
    ]
