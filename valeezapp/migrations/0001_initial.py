# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garment',
            fields=[
                ('garment_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('layer', models.PositiveIntegerField()),
                ('type_bformal', models.BooleanField()),
                ('type_bcasual', models.BooleanField()),
                ('type_vacation', models.BooleanField()),
                ('rain', models.BooleanField()),
                ('snow', models.BooleanField()),
                ('icon', models.ImageField(width_field=100, height_field=100, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Toiletry',
            fields=[
                ('toiletries_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('trip_duration', models.PositiveIntegerField()),
                ('icon', models.ImageField(width_field=100, height_field=100, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.AutoField(serialize=False, primary_key=True)),
                ('destination', models.CharField(max_length=40)),
                ('depart_date', models.TimeField()),
                ('return_date', models.TimeField()),
                ('trip_type', models.CharField(max_length=15, choices=[('type_bformal', 'Business formal'), ('type_bcasual', 'Business casual'), ('type_vacation', 'Vacation')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6, choices=[('male', 'male'), ('female', 'female')])),
                ('email', models.CharField(max_length=75)),
                ('mobile', models.PositiveIntegerField()),
                ('home_timezone', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Valeez',
            fields=[
                ('valeez_id', models.AutoField(serialize=False, primary_key=True)),
                ('garments', models.ManyToManyField(to='valeezapp.Garment')),
                ('toiletries', models.ManyToManyField(to='valeezapp.Toiletry')),
                ('trip_id', models.ForeignKey(to='valeezapp.Trip')),
                ('user_id', models.ForeignKey(to='valeezapp.User')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='user_id',
            field=models.ForeignKey(to='valeezapp.User'),
        ),
    ]
