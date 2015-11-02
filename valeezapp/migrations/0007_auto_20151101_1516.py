# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0006_auto_20151101_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='valeez',
            name='id',
            field=models.AutoField(default=1, primary_key=True, verbose_name='ID', auto_created=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voyage',
            name='id',
            field=models.AutoField(default=1, primary_key=True, verbose_name='ID', auto_created=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='valeez',
            name='user_id',
            field=models.OneToOneField(to='valeezapp.User'),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='user_id',
            field=models.OneToOneField(to='valeezapp.User'),
        ),
    ]
