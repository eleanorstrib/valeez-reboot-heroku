# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0022_auto_20151123_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garment',
            name='temp',
        ),
        migrations.AddField(
            model_name='garment',
            name='temp_cold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='garment',
            name='temp_high',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='garment',
            name='temp_medcold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='garment',
            name='temp_medhigh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='garment',
            name='temp_temp',
            field=models.BooleanField(default=False),
        ),
    ]
