# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0007_auto_20151101_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valeez',
            name='user_id',
            field=models.OneToOneField(to='valeezapp.User', null=True),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='user_id',
            field=models.OneToOneField(to='valeezapp.User', null=True),
        ),
    ]
