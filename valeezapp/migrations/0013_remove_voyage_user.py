# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0012_auto_20151101_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voyage',
            name='user',
        ),
    ]
