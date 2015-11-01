# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0003_auto_20151029_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valeez',
            name='valeez_id',
        ),
        migrations.AlterField(
            model_name='valeez',
            name='user_id',
            field=models.OneToOneField(serialize=False, primary_key=True, to='valeezapp.User'),
        ),
    ]
