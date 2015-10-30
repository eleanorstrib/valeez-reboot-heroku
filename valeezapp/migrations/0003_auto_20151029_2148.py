# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0002_auto_20151025_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='user_id',
            field=models.ForeignKey(default=None, null=True, to='valeezapp.User', blank=True),
        ),
    ]
