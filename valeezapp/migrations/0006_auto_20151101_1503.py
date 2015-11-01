# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0005_auto_20151101_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garment',
            name='garment_id',
        ),
        migrations.RemoveField(
            model_name='toiletry',
            name='toiletries_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='voyage',
            name='voyage_id',
        ),
        migrations.AddField(
            model_name='garment',
            name='id',
            field=models.AutoField(default=1, auto_created=True, primary_key=True, verbose_name='ID', serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='toiletry',
            name='id',
            field=models.AutoField(default=1, auto_created=True, primary_key=True, verbose_name='ID', serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(default=1, auto_created=True, primary_key=True, verbose_name='ID', serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voyage',
            name='user_id',
            field=models.OneToOneField(default=1, primary_key=True, to='valeezapp.User', serialize=False),
        ),
    ]
