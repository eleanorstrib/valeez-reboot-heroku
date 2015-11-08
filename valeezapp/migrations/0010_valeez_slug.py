# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0009_auto_20151107_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='valeez',
            name='slug',
            field=models.SlugField(unique=True, default=1),
            preserve_default=False,
        ),
    ]
