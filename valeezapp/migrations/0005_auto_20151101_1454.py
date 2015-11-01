# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0004_auto_20151101_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='user_id',
            field=models.OneToOneField(to='valeezapp.User', primary_key=True, default=1),
        ),
    ]
