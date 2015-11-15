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
	user = m.ForeignKey(User, unique=False)
	DESTINATION_CHOICES = (
		('TX/Austin', 'Austin, TX'),
		('NC/Charlotte', 'Charlotte, NC'),
		('IL/Chicago', 'Chicago, IL'),
		('OH/Columbus', 'Columbus, OH'),
		('TX/Dallas', 'Dallas/Fort Worth, TX'),
		('CO/Denver', 'Denver, CO'),
		('MI/Detroit', 'Detroit, MI'),
		('TX/El_Paso', 'El Paso, TX'),
		('TX/Houston', 'Houston, TX'),
		('IN/Indianapolis', 'Indianapolis, IN'),
		('FL/Jacksonville', 'Jacksonville, FL'),
		('NV/Las_Vegas', 'Las Vegas, NV'),
		('CA/Los_Angeles', 'Los Angeles, CA'),
		('AZ/Pheonix', 'Pheonix, AZ'),
		('PA/Philadelphia', 'Philadelphia, PA'),
		('NY/New_York', 'New York, NY'),
		('TX/San_Antonio', 'San Antonio, TX'),
		('CA/San_Diego', 'San Diego, CA'),
		('CA/San_Francisco', 'San Francisco, CA'),
		('CA/San_Jose', 'San Jose, CA'),
		('WA/Seattle', 'Seattle, WA'),
		('DC/Washington', 'Washington, DC'),
		)
	destination = m.CharField(max_length=100, choices=DESTINATION_CHOICES)
	depart_date = m.DateField()
	return_date = m.DateField()
	VOYAGE_TYPE_CHOICES = (
		('type_bformal', 'Business formal'),
		('type_bcasual', 'Business casual'),
		('type_vacation', 'Vacation'),
	)
	voyage_type = m.CharField(max_length=100, choices=VOYAGE_TYPE_CHOICES, default='type_bcasual')
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
		('temp_all', 'All temps'),
	)
	temp = m.CharField(max_length=25, choices=TEMP_CHOICES, default='temp_all')
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
	slug = m.SlugField(unique=True)

	def __str__(self):
		return self.valeez_id

