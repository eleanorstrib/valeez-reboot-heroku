
import json
import requests
import time
import os
import wardrobe as w
from pprint import pprint

WU_KEY = os.environ['WU_KEY']
trip_dates = ""
# FIXME: temp variables for testing
user_destination = "IT/Rome" #string
user_trip_type = "vacation" #string
user_depart = "01/02/2016" #string converted to datetime
user_return = "09/02/2016" #string converted to datetime
user_gender = "female" #string

#set up of classes
# takes details of trip from front end, converts dates
class Trip(object):
	def __init__(self, user_destination, user_trip_type, user_depart, user_return, user_gender):
		self.destination = user_destination
		self.type = user_trip_type
		self.departing = time.strptime(user_depart, "%d/%m/%Y")
		self.returning = time.strptime(user_return, "%d/%m/%Y")
		self.duration = self.returning.tm_yday - self.departing.tm_yday
		self.gender = user_gender
	
	def info(self):
		print ("User provided the following details for this trip:")
		print ("Destination:", self.destination)
		print ("Depart %s, return %s for a duration of %d days" % (user_depart, user_return, self.duration))
		print( "User dresses as a", self.gender)

# gets forecast from WU API
class Forecast(object):
	def __init__(self, user_destination):
		self.destination = user_destination

	def get_forecast(self, API_PLAN_URL, WU_KEY, trip_dates):
		self.forecastr= requests.get(API_PLAN_URL+self.destination+".json")
		self.forecastdata = self.forecastr.json()
		return self.forecastdata

	def summarize_data(self, Ti):
		self.data = self.get_forecast(API_URL, WU_KEY)
		print()
		

class Valeez(object):
	pass



# FIXME: class instantiation and prints for testing
trip1 = Trip(user_destination, user_trip_type, user_depart, user_return, user_gender)
pprint (vars(trip1))

# FIXME: Test that Trip class working
# print "this is the instantiation of the class Trip"

# this section grabs the dates from the datetime object created
dates_convert = [
	('depart_month', str(trip1.departing.tm_mon)),
	('depart_day', str(trip1.departing.tm_mday)),
	('return_month', str(trip1.returning.tm_mon)),
	('return_day', str(trip1.returning.tm_mday))
]

# this loop creates a string to use in the API call
for item in dates_convert:
	if len(item[1]) == 1:
		trip_dates = trip_dates + "0" + item[1]
	else:
		trip_dates = trip_dates + item[1]

API_PLAN_URL="http://api.wunderground.com/api/"+WU_KEY+"/planner_" + trip_dates + "/q/"

print ("trip_dates", trip_dates)

forecast1 = Forecast(user_destination).get_forecast(API_PLAN_URL, WU_KEY, trip_dates)
summary_forecast = {
					'max_temp_f': int(forecast1[u'trip'][u'temp_high'][u'max'][u'F']),
					'max_temp_c': int(forecast1[u'trip'][u'temp_high'][u'max'][u'C']),
					'avg_temp_f': int(forecast1[u'trip'][u'temp_high'][u'avg'][u'F']),
					'avg_temp_c': int(forecast1[u'trip'][u'temp_high'][u'avg'][u'C']),
					'min_temp_f': int(forecast1[u'trip'][u'temp_low'][u'min'][u'F']),
					'min_temp_f': int(forecast1[u'trip'][u'temp_low'][u'min'][u'C']),					
					'precip': int(forecast1[u'trip'][u'chance_of'][u'chanceofrainday'][u'percentage']),
					'snow': int(forecast1[u'trip'][u'chance_of'][u'chanceofsnowday'][u'percentage'])
					}
print (summary_forecast)
