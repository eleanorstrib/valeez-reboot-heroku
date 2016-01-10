# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0017_auto_20151120_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valeez',
            name='garments',
        ),
        migrations.AddField(
            model_name='valeez',
            name='garments',
            field=models.CharField(max_length=2000, default=1),
        ),
        migrations.RemoveField(
            model_name='valeez',
            name='toiletries',
        ),
        migrations.AddField(
            model_name='valeez',
            name='toiletries',
            field=models.CharField(max_length=2000, default=1),
        ),
    ]
