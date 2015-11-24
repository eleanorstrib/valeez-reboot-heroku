# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0020_remove_valeez_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='valeez',
            name='slug',
            field=models.SlugField(verbose_name=models.OneToOneField(related_name='voyage', to='valeezapp.Voyage'), default=0),
            preserve_default=False,
        ),
    ]
