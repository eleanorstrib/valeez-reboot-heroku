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
                ('garment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75)),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('layer', models.IntegerField()),
                ('type_bformal', models.BooleanField()),
                ('type_bcasual', models.BooleanField()),
                ('type_vacation', models.BooleanField()),
                ('temp', models.CharField(choices=[('temp_high', 'Hot'), ('temp_medhigh', 'Warm'), ('temp_temp', 'Temperate'), ('temp_medcold', 'Cold'), ('temp_cold', 'Very cold')], max_length=25, default='temp_cold')),
                ('rain', models.BooleanField()),
                ('snow', models.BooleanField()),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Toiletry',
            fields=[
                ('toiletries_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('trip_duration', models.IntegerField()),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
                ('email', models.CharField(max_length=75)),
                ('mobile', models.CharField(max_length=10)),
                ('home_timezone', models.CharField(choices=[('America/Los_Angeles', 'Pacific'), ('America/Denver', 'Mountain'), ('America/Chicago', 'Central'), ('America/New_York', 'Eastern')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Valeez',
            fields=[
                ('valeez_id', models.AutoField(primary_key=True, serialize=False)),
                ('garments', models.ManyToManyField(to='valeezapp.Garment')),
                ('toiletries', models.ManyToManyField(to='valeezapp.Toiletry')),
                ('user_id', models.ForeignKey(to='valeezapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('voyage_id', models.AutoField(primary_key=True, serialize=False)),
                ('destination', models.CharField(max_length=40)),
                ('depart_date', models.DateField()),
                ('return_date', models.DateField()),
                ('voyage_type', models.CharField(choices=[('type_bformal', 'Business formal'), ('type_bcasual', 'Business casual'), ('type_vacation', 'Vacation')], max_length=15)),
                ('user_id', models.ForeignKey(to='valeezapp.User')),
            ],
        ),
        migrations.AddField(
            model_name='valeez',
            name='voyage_id',
            field=models.ForeignKey(to='valeezapp.Voyage'),
        ),
    ]
