# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0009_auto_20151101_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valeez',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='voyage',
            name='user_id',
        ),
        migrations.AddField(
            model_name='valeez',
            name='user',
            field=models.ForeignKey(to='valeezapp.User', null=True, default=1),
        ),
        migrations.AddField(
            model_name='voyage',
            name='user',
            field=models.ForeignKey(to='valeezapp.User', default=1),
        ),
    ]
