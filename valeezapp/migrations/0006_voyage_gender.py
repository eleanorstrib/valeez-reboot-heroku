# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0005_auto_20151105_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='voyage',
            name='gender',
            field=models.CharField(max_length=6, choices=[('female', 'Female'), ('male', 'Male')], default='female'),
        ),
    ]
