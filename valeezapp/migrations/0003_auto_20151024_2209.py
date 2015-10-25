# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0002_auto_20151021_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='garment',
            name='temp',
            field=models.CharField(choices=[('temp_high', 'Hot'), ('temp_medhigh', 'Warm'), ('temp_temp', 'Temperate'), ('temp_medcold', 'Cold'), ('temp_cold', 'Very cold')], max_length=25, default='temp_cold'),
        ),
        migrations.AlterField(
            model_name='garment',
            name='layer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='toiletry',
            name='trip_duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='depart_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='return_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='home_timezone',
            field=models.CharField(choices=[('America/Los_Angeles', 'Pacific'), ('America/Denver', 'Mountain'), ('America/Chicago', 'Central'), ('America/New_York', 'Eastern')], max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
