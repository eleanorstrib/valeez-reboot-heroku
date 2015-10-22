# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garment',
            name='icon',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='toiletry',
            name='icon',
            field=models.ImageField(upload_to=''),
        ),
    ]
