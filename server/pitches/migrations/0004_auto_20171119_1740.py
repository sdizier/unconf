# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pitches', '0003_auto_20171119_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitch',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created at'),
        ),
    ]
