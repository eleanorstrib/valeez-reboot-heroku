from django.db import models as m
from django.contrib.auth.models import User
import datetime
		
class Voyage(m.Model):
	user = m.ForeignKey(User)
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
	user = m.ForeignKey(User, null=True)
	voyage = m.OneToOneField(Voyage, null=True)
	garments = m.ManyToManyField(Garment)
	toiletries = m.ManyToManyField(Toiletry)

	def __str__(self):
		return self.valeez_id

