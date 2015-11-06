# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='users'),
        ),
        migrations.AlterField(
            model_name='valeez',
            name='voyage',
            field=models.OneToOneField(default=1, to='valeezapp.Voyage', related_name='voyage'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voyage',
            name='user',
            field=models.ForeignKey(default=1, to='valeezapp.UserProfile', related_name='users'),
            preserve_default=False,
        ),
    ]
