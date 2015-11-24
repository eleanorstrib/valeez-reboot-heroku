# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0018_auto_20151123_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='valeez',
            old_name='garments',
            new_name='contents',
        ),
        migrations.RemoveField(
            model_name='valeez',
            name='toiletries',
        ),
    ]
