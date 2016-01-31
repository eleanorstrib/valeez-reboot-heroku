# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valeezapp', '0025_demovoyage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voyage',
            name='destination',
            field=models.CharField(choices=[('TX/Austin', 'Austin, TX'), ('Canada/Calgary', 'Calgary, AB'), ('NC/Charlotte', 'Charlotte, NC'), ('IL/Chicago', 'Chicago, IL'), ('OH/Columbus', 'Columbus, OH'), ('TX/Dallas', 'Dallas/Fort Worth, TX'), ('CO/Denver', 'Denver, CO'), ('MI/Detroit', 'Detroit, MI'), ('TX/El_Paso', 'El Paso, TX'), ('Canada/Halifax', 'Halifax, NS'), ('TX/Houston', 'Houston, TX'), ('IN/Indianapolis', 'Indianapolis, IN'), ('FL/Jacksonville', 'Jacksonville, FL'), ('NV/Las_Vegas', 'Las Vegas, NV'), ('CA/Los_Angeles', 'Los Angeles, CA'), ('Canada/Montreal', 'Montreal, PQ'), ('AZ/Phoenix', 'Phoenix, AZ'), ('PA/Philadelphia', 'Philadelphia, PA'), ('NY/New_York', 'New York, NY'), ('TX/San_Antonio', 'San Antonio, TX'), ('CA/San_Diego', 'San Diego, CA'), ('CA/San_Francisco', 'San Francisco, CA'), ('CA/San_Jose', 'San Jose, CA'), ('WA/Seattle', 'Seattle, WA'), ('Canada/Toronto', 'Toronto, ON'), ('Canada/Vancouver', 'Vancouver, BC'), ('DC/Washington', 'Washington, DC'), ('Canada/Winnipeg', 'Winnipeg, MB')], max_length=100),
        ),
    ]
