from django.db import models as m
import datetime

class User(m.Model):
	user_id = m.AutoField(primary_key=True)
	username = m.CharField(max_length=25)
	password = m.CharField(max_length=20)
	GENDER_CHOICES = (
		("male", "male"),
		("female", "female"),
		)
	gender = m.CharField(max_length=6, choices=GENDER_CHOICES)
	email = m.CharField(max_length=75)
	mobile = m.CharField(max_length=10)
	TIMEZONE_CHOICES = (
		('America/Los_Angeles', 'Pacific'),
		('America/Denver', 'Mountain'),
		('America/Chicago', 'Central'),
		('America/New_York', 'Eastern'),
	)
	home_timezone = m.CharField(max_length=50, choices=TIMEZONE_CHOICES)

	def __str__(self):
		return self.username
		
class Voyage(m.Model):
	voyage_id = m.AutoField(primary_key=True)
	user_id = m.ForeignKey(User)
	destination = m.CharField(max_length=40)
	depart_date = m.DateField()
	return_date = m.DateField()
	VOYAGE_TYPE_CHOICES = (
		('type_bformal', 'Business formal'),
		('type_bcasual', 'Business casual'),
		('type_vacation', 'Vacation'),
	)
	voyage_type = m.CharField(max_length=15, choices=VOYAGE_TYPE_CHOICES)
	
	def __str__(self):
		return self.destination

class Garment(m.Model):
	garment_id = m.AutoField(primary_key=True)
	name = m.CharField(max_length=75)
	male = m.BooleanField()
	female = m.BooleanField()
	layer = m.IntegerField()
	type_bformal = m.BooleanField()
	type_bcasual = m.BooleanField()
	type_vacation = m.BooleanField()
	TEMP_CHOICES = (
		('temp_high', 'Hot'),
		('temp_medhigh', 'Warm'),
		('temp_temp', 'Temperate'),
		('temp_medcold', 'Cold'),
		('temp_cold', 'Very cold'),
	)
	temp = m.CharField(max_length=25, choices=TEMP_CHOICES, default='temp_cold')
	rain = m.BooleanField()
	snow = m.BooleanField()

	def __str__(self):
		return  self.name

class Toiletry(m.Model):
	toiletries_id = m.AutoField(primary_key=True)
	name = m.CharField(max_length=50)
	male = m.BooleanField()
	female = m.BooleanField()
	trip_duration = m.IntegerField()

	def __str__(self):
		return self.name

class Valeez(m.Model):
	valeez_id = m.AutoField(primary_key=True)
	user_id = m.ForeignKey(User)
	voyage_id = m.ForeignKey(Voyage)
	garments = m.ManyToManyField(Garment)
	toiletries = m.ManyToManyField(Toiletry)

	def __str__(self):
		return self.valeez_id

