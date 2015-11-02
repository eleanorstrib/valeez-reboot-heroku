# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0008_auto_20151101_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='user_id',
            field=models.ForeignKey(null=True, default=1, to='valeezapp.User'),
        ),
    ]
