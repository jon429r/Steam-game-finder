# Generated by Django 4.2.6 on 2023-11-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_rename_negative_game_negative_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='metacritic_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
