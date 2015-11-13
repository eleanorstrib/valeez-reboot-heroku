# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0011_auto_20151107_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='voyage_type',
            field=models.CharField(default='type_bcasual', choices=[('type_bformal', 'Business formal'), ('type_bcasual', 'Business casual'), ('type_vacation', 'Vacation')], max_length=100),
        ),
    ]
