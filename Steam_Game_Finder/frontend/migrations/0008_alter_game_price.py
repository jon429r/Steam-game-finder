# Generated by Django 4.2.6 on 2023-11-17 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_alter_game_mac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
