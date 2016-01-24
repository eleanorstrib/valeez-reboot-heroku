from django.db import models as m
from django.contrib.auth.models import User
import datetime


class Voyage(m.Model):
	"""
	This is the model for the form the user completes to make a
	new valeez.
	"""
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
		('AZ/Phoenix', 'Phoenix, AZ'),
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
	query = m.CharField(max_length=200, default="")

	def __str__(self):
		return self.destination


class Demovoyage(m.Model):
	"""
	This is the model for the form a demo user completes to make a
	new valeez.
	"""
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
		('AZ/Phoenix', 'Phoenix, AZ'),
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
	query = m.CharField(max_length=200, default="")

	def __str__(self):
		return self.destination

class Valeez(m.Model):
	"""
	Instances of this class are instantiated when a Valeez is created
	and saved in the database.
	"""
	voyage = m.OneToOneField(Voyage, related_name="voyage")
	contents = m.CharField(max_length=2000, default=1)

	def __str__(self):
		return self.contents


class Garment(m.Model):
	"""
	This is the model for all garments that will go in the valeez.
	These are stored in the database, queried and added to the valeez
	when the user submits the Voyage form.
	"""
	name = m.CharField(max_length=75)
	male = m.BooleanField()
	female = m.BooleanField()
	layer = m.IntegerField()
	# voyage type
	type_bformal = m.BooleanField()
	type_bcasual = m.BooleanField()
	type_vacation = m.BooleanField()
	# temp
	temp_high = m.BooleanField(default=False)
	temp_medhigh = m.BooleanField(default=False)
	temp_temp = m.BooleanField(default=False)
	temp_medcold = m.BooleanField(default=False)
	temp_cold = m.BooleanField(default=False)
	# weather conditions
	rain = m.BooleanField()
	snow = m.BooleanField()

	def __str__(self):
		return  self.name


class Toiletry(m.Model):
	"""
	This is the model for all toiletries (anything that's not clothing 
	or an accessory) that will go in the valeez.
	These are stored in the database, queried and added to the valeez
	when the user submits the Voyage form.
	"""
	name = m.CharField(max_length=50)
	male = m.BooleanField()
	female = m.BooleanField()
	trip_duration = m.IntegerField()

	def __str__(self):
		return self.name




