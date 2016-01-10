# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0013_auto_20151114_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garment',
            name='temp',
            field=models.CharField(choices=[('temp_high', 'Hot'), ('temp_medhigh', 'Warm'), ('temp_temp', 'Temperate'), ('temp_medcold', 'Cold'), ('temp_cold', 'Very cold'), ('temp_all', 'All temps')], max_length=25, default='temp_cold'),
        ),
    ]
