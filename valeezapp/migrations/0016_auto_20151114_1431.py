# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0015_auto_20151114_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garment',
            name='gender',
        ),
        migrations.AddField(
            model_name='garment',
            name='female',
            field=models.BooleanField(default='female'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='garment',
            name='male',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
