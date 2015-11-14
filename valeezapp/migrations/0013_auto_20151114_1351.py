# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0012_auto_20151112_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garment',
            name='female',
        ),
        migrations.RemoveField(
            model_name='garment',
            name='male',
        ),
        migrations.AddField(
            model_name='garment',
            name='gender',
            field=models.CharField(max_length=6, default='female', choices=[('female', 'Female'), ('male', 'Male')]),
        ),
    ]
