# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0010_auto_20151101_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valeez',
            name='user',
        ),
        migrations.RemoveField(
            model_name='valeez',
            name='voyage_id',
        ),
        migrations.RemoveField(
            model_name='voyage',
            name='user',
        ),
    ]
