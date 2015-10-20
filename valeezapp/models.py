from django.db import models as m
import datetime

class Users(m.Model):
	userid = m.AutoField(primary_key=true)
	username = m.CharField(max_length=25)
	password = m.CharField(max_length=12)
	email = m.CharField(max_length=75)
	mobile = m.PositiveIntegerField(maxlength=11)
	home_timezone = m.CharField(max_length=40)

class Trip(m.model):
	destination = m.CharField(max_length=40)
	depart_date = m.TimeField
	return_date = m.TimeField
	TRIP_TYPE_CHOICES = (
		(type_bformal, 'Business formal'),
		(type_bcasual, 'Business casual'),
		(type_vacation, 'Vacation'),
		)
	trip_type = m.CharField(choices=TRIP_TYPE_CHOICES)

class Garments(m.Model):
	name = m.CharField(max_length=75)
	male = m.BooleanField
	female = m.BooleanField
	layer = m.PositiveIntegerField(lower=0, upper=5)
	type_bformal = m.BooleanField
	type_bcasual = m.BooleanField
	type_vacation = m. BooleanField
	rain = m.BooleanField
	snow = m.BooleanField
	icon = m.ImageField (height_field=100, widthfield=100)

class Toiletries(m.Model):
	male = m.BooleanField
	female = m.BooleanField
	trip_duration = m.PositiveIntegerField
	icon = m.ImageField
