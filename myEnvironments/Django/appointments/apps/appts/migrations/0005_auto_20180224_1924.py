# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-24 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appts', '0004_auto_20180223_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appts',
            old_name='tasks',
            new_name='task',
        ),
        migrations.AlterField(
            model_name='appts',
            name='time',
            field=models.CharField(max_length=255),
        ),
    ]