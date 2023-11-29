# Generated by Django 4.2.6 on 2023-11-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0012_alter_developer_app_id_alter_publisher_app_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='app_id',
        ),
        migrations.RemoveField(
            model_name='language',
            name='app_id',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='app_id',
        ),
        migrations.AlterField(
            model_name='developer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.TextField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='language',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
