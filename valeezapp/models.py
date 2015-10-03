from django.db import models as m
import datetime

class User(models.Model):
	username = m.CharField(max_length=25)
	password = m.CharField(max_length=12)
	email = m.CharField(max_length=75)
	mobile = m.IntegerField(maxlength=11)
	home_timezone = m.CharField(max_length=30)

class Garment(models.Model):
	name = m.CharField(max_length=75)
	male_wardrobe = m.BooleanField
	female_wardrobe = m.BooleanField
	layer = m.IntegerField
	type_bformal = m.BooleanField
	type_bcasual = m.BooleanField
	type_vacation = m. BooleanField
	rain = m.BooleanField
	snow = m.BooleanField
