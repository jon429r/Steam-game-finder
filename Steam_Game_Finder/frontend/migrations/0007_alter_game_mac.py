# Generated by Django 4.2.6 on 2023-11-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_alter_game_linux'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='mac',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]