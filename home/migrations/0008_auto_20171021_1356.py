# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20171021_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contests',
            name='total_score',
        ),
        migrations.AddField(
            model_name='questions',
            name='score_secured',
            field=models.IntegerField(default=0),
        ),
    ]