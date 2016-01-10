# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0003_auto_20151105_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='user',
            field=models.ForeignKey(unique=True, to='valeezapp.UserProfile'),
        ),
    ]
