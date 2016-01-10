# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0019_auto_20151123_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valeez',
            name='slug',
        ),
    ]
