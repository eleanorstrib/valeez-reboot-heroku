from django.db import models as m
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

import datetime

# this class creates a one to one relationship with the auth model's User
# purpose is to add extra fields relevant to the user in this app
class UserProfile(m.Model):
	user = m.OneToOneField(User, unique=True)
	mobile = PhoneNumberField()
	GENDER_PREF_CHOICES = (
		('female', 'Female'),
		('male', 'Male'),
		)
	gender = m.CharField(max_length=6, choices=GENDER_PREF_CHOICES)

	def __str___(self):
		return self.user
		
class Voyage(m.Model):
	user = m.OneToOneField(User, unique=True)
	destination = m.CharField(max_length=40)
	depart_date = m.DateField()
	return_date = m.DateField()
	VOYAGE_TYPE_CHOICES = (
		('type_bformal', 'Business formal'),
		('type_bcasual', 'Business casual'),
		('type_vacation', 'Vacation'),
	)
	voyage_type = m.CharField(max_length=15, choices=VOYAGE_TYPE_CHOICES)
	GENDER_PREF_CHOICES = (
		('female', 'Female'),
		('male', 'Male'),
		)
	gender = m.CharField(max_length=6, choices=GENDER_PREF_CHOICES, default="female")

	
	def __str__(self):
		return self.destination

class Garment(m.Model):
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
	name = m.CharField(max_length=50)
	male = m.BooleanField()
	female = m.BooleanField()
	trip_duration = m.IntegerField()

	def __str__(self):
		return self.name

class Valeez(m.Model):
	voyage = m.OneToOneField(Voyage, related_name="voyage")
	garments = m.ManyToManyField(Garment)
	toiletries = m.ManyToManyField(Toiletry)

	def __str__(self):
		return self.valeez_id

