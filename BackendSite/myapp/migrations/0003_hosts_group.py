# Generated by Django 3.0.1 on 2019-12-25 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20191225_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosts',
            name='group',
            field=models.CharField(default='default', max_length=255, verbose_name='组'),
        ),
    ]