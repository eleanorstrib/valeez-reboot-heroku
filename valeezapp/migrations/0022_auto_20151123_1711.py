# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0021_valeez_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valeez',
            name='slug',
        ),
        migrations.AddField(
            model_name='voyage',
            name='query',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
