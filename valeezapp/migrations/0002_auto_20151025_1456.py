# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garment',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='toiletry',
            name='icon',
        ),
    ]
