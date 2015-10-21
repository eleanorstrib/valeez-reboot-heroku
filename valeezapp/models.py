from django.db import models as m
import datetime

class Users(m.Model):
	user_id = m.AutoField(primary_key=True)
	username = m.CharField(max_length=25)
	password = m.CharField(max_length=20)
	GENDER_CHOICES = (
		("male", "male"),
		("female", "female"),
		)
	gender = m.CharField(choices=GENDER_CHOICES)
	email = m.CharField(max_length=75)
	mobile = m.PositiveIntegerField(max_length=11)
	home_timezone = m.CharField(max_length=40)
	trips = m.OneToManyField(Trip)
	valeez = m.OneToManyField(Valeez)

	def __str__(self):
		return 'user_id %s username %s password %s gender %s email %s mobile %s timezone %s' % (self.user_id, self.username, self.password, self.gender, self.email, self.mobile, self.home_timezone)

class Trip(m.Model):
	trip_id = m.AutoField(primary_key=True)
	user_id = m.ForeignKey('User.user_id')
	destination = m.CharField(max_length=40)
	depart_date = m.TimeField
	return_date = m.TimeField
	TRIP_TYPE_CHOICES = (
		(type_bformal, 'Business formal'),
		(type_bcasual, 'Business casual'),
		(type_vacation, 'Vacation'),
		)
	trip_type = m.CharField(choices=TRIP_TYPE_CHOICES)
	
	def __str__(self):
		return 'trip_id %s user_id %s destination %s depart_date %s return_date %s trip_type %s' % (self.trip_id, self.user_id, self.destination, self.depart_date, self.return_date, self.trip_type)

class Valeez(m.Model):
	valeez_id = m.AutoField(primary_key=True)
	user_id = m.ForeignKey('User.user_id')
	trip_id = m.ForeignKey('Trip.trip_id')
	garments = m.ManyToManyField(Garments)
	toiletries = m.ManyToManyField(Toiletries)

	def __str__(self):
		return 'primary %s user_id %s trip_id %s garments %s toiletries %s' % (self.valeez_id, self.user_id, self.trip_id, self.garments, self.toiletries)


class Garments(m.Model):
	garment_id = m.AutoField(primary_key=True)
	name = m.CharField(max_length=75)
	male = m.BooleanField
	female = m.BooleanField
	layer = m.PositiveIntegerField(lower=0, upper=5)
	type_bformal = m.BooleanField
	type_bcasual = m.BooleanField
	type_vacation = m. BooleanField
	rain = m.BooleanField
	snow = m.BooleanField
	icon = m.ImageField (height_field=100, width_field=100)

	def __str__(self):
		return 'name %s female %s layer %s type_bformal %s type_bcasual %s type_vacation' % (self.name, self.female, self.layer, self.type_bformal, self.type_bcasual, self.type_vacation)

class Toiletries(m.Model):
	toiletries_id = m.AutoField(primary_key=True)
	name = m.CharField(max_length=50)
	male = m.BooleanField
	female = m.BooleanField
	trip_duration = m.PositiveIntegerField
	icon = m.ImageField

	def __str__(self):
		return 'name %s female %s trip_duration %s' % (self.name, self.female, self.trip_duration)