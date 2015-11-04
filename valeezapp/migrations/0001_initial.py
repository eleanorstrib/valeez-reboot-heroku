# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Garment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
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
            ],
        ),
        migrations.CreateModel(
            name='Toiletry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('male', models.BooleanField()),
                ('female', models.BooleanField()),
                ('trip_duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=6)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Valeez',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('garments', models.ManyToManyField(to='valeezapp.Garment')),
                ('toiletries', models.ManyToManyField(to='valeezapp.Toiletry')),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('destination', models.CharField(max_length=40)),
                ('depart_date', models.DateField()),
                ('return_date', models.DateField()),
                ('voyage_type', models.CharField(choices=[('type_bformal', 'Business formal'), ('type_bcasual', 'Business casual'), ('type_vacation', 'Vacation')], max_length=15)),
                ('user', models.ForeignKey(null=True, to='valeezapp.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='valeez',
            name='voyage',
            field=models.OneToOneField(null=True, to='valeezapp.Voyage'),
        ),
    ]
