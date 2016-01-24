# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0024_auto_20160113_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demovoyage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('destination', models.CharField(choices=[('TX/Austin', 'Austin, TX'), ('NC/Charlotte', 'Charlotte, NC'), ('IL/Chicago', 'Chicago, IL'), ('OH/Columbus', 'Columbus, OH'), ('TX/Dallas', 'Dallas/Fort Worth, TX'), ('CO/Denver', 'Denver, CO'), ('MI/Detroit', 'Detroit, MI'), ('TX/El_Paso', 'El Paso, TX'), ('TX/Houston', 'Houston, TX'), ('IN/Indianapolis', 'Indianapolis, IN'), ('FL/Jacksonville', 'Jacksonville, FL'), ('NV/Las_Vegas', 'Las Vegas, NV'), ('CA/Los_Angeles', 'Los Angeles, CA'), ('AZ/Phoenix', 'Phoenix, AZ'), ('PA/Philadelphia', 'Philadelphia, PA'), ('NY/New_York', 'New York, NY'), ('TX/San_Antonio', 'San Antonio, TX'), ('CA/San_Diego', 'San Diego, CA'), ('CA/San_Francisco', 'San Francisco, CA'), ('CA/San_Jose', 'San Jose, CA'), ('WA/Seattle', 'Seattle, WA'), ('DC/Washington', 'Washington, DC')], max_length=100)),
                ('depart_date', models.DateField()),
                ('return_date', models.DateField()),
                ('voyage_type', models.CharField(choices=[('type_bformal', 'Business formal'), ('type_bcasual', 'Business casual'), ('type_vacation', 'Vacation')], max_length=100, default='type_bcasual')),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=6, default='female')),
                ('query', models.CharField(max_length=200, default='')),
            ],
        ),
    ]
