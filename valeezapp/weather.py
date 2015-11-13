
import json
import requests
import time
import os
from django.contrib.auth.models import User
from .models import Garment, Toiletry, Valeez, Voyage
import .views as v

# WU_KEY = os.environ.get['WU_API_KEY']
# API_URL = "http://api.wunderground.com/api/%s/planner_%s/q/%s.json"


user = v.show_valeez.this_user
destination = Voyage.objects.filter(user=this_user).latest('destination')

# depart_date = Voyage.depart_date
# return_date = Voyage.return_date
# print(destination, depart_date, return_date)
# #DATES format is MMDDMMDD
# def get_dates_api_format(depart_date, return_date):
# 	pass




# class Forecast(object):
# 	def __init__(self, destination):
# 		self.destination = destination

# 	def get_forecast(self, API_URL, WU_KEY, destination, depart_date, return_date):
# 		self.forecast= requests.get(API_URL % (WU_KEY, depart))
# 		self.forecastdata = self.forecastr.json()
# 		return self.forecastdata

# 	def summarize_data(self, Ti):
# 		self.data = self.get_forecast(API_URL, WU_KEY)
# 		print()
		


# # FIXME: class instantiation and prints for testing
# trip1 = Trip(user_destination, user_trip_type, user_depart, user_return, user_gender)
# pprint (vars(trip1))

# # FIXME: Test that Trip class working
# # print "this is the instantiation of the class Trip"

# # this section grabs the dates from the datetime object created
# dates_convert = [
# 	('depart_month', str(trip1.departing.tm_mon)),
# 	('depart_day', str(trip1.departing.tm_mday)),
# 	('return_month', str(trip1.returning.tm_mon)),
# 	('return_day', str(trip1.returning.tm_mday))
# ]

# # this loop creates a string to use in the API call
# for item in dates_convert:
# 	if len(item[1]) == 1:
# 		trip_dates = trip_dates + "0" + item[1]
# 	else:
# 		trip_dates = trip_dates + item[1]

# API_PLAN_URL="http://api.wunderground.com/api/"+WU_KEY+"/planner_" + trip_dates + "/q/"

# print ("trip_dates", trip_dates)

# forecast1 = Forecast(user_destination).get_forecast(API_PLAN_URL, WU_KEY, trip_dates)
# summary_forecast = {
# 					'max_temp_f': int(forecast1[u'trip'][u'temp_high'][u'max'][u'F']),
# 					'max_temp_c': int(forecast1[u'trip'][u'temp_high'][u'max'][u'C']),
# 					'avg_temp_f': int(forecast1[u'trip'][u'temp_high'][u'avg'][u'F']),
# 					'avg_temp_c': int(forecast1[u'trip'][u'temp_high'][u'avg'][u'C']),
# 					'min_temp_f': int(forecast1[u'trip'][u'temp_low'][u'min'][u'F']),
# 					'min_temp_f': int(forecast1[u'trip'][u'temp_low'][u'min'][u'C']),					
# 					'precip': int(forecast1[u'trip'][u'chance_of'][u'chanceofrainday'][u'percentage']),
# 					'snow': int(forecast1[u'trip'][u'chance_of'][u'chanceofsnowday'][u'percentage'])
# 					}
# print (summary_forecast)
