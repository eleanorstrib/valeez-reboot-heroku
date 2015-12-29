
import os
import time
import requests
import ast
import datetime
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from valeezapp.models import UserProfile, Voyage, Valeez, Garment, Toiletry
from django.template.defaultfilters import slugify
from .forms import UserForm, UserProfileForm, VoyageForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


# global variables, used in show_valeez
WU_KEY = os.environ.get('WU_API_KEY')
API_URL_TEN_DAY = "http://api.wunderground.com/api/%s/forecast10day/q/%s.json"
API_URL_PLAN = "http://api.wunderground.com/api/%s/planner_%s/q/%s.json"


def index(request):
	"""
	This view renders the index page and retrieves user data for display in the header.
	"""
	user = request.user
	return render(request, 'valeezapp/index.html', {'user': user})


def make_valeez(request):
	"""
	Shows form created with the model, associates user with destination, travel dates, etc
	and saves data to the database.
	"""
	form = VoyageForm()
	if request.method == 'POST':
		form = VoyageForm(request.POST)
		if form.is_valid():
			# form.save()
			link_user = form.save(commit=False)
			link_user.user = request.user
			link_user.save()
			return HttpResponseRedirect('/show_valeez/')
	return render(request, 'valeezapp/make_valeez.html', {'form': form})


def show_valeez(request):
	""" 
	This view takes data from the form in make_valeez, calls the Weather Underground API
	and uses the weather data to create the packing list.
	"""
	# data about the user and the voyage needed to create the valeez and display data
	this_user = request.user
	user_today_date = datetime.date.today()
	
	# last voyage created by this user
	user_voyages = Voyage.objects.filter(user=this_user).order_by('-id')
	
	destination = user_voyages[0].destination
	destination_pretty = (str(destination)[3:]).replace('_', ' ')
	
	depart_date = user_voyages[0].depart_date
	return_date = user_voyages[0].return_date
	depart_delta = (depart_date - user_today_date).days
	return_delta = (return_date - user_today_date).days
	duration = ((return_date - depart_date).days) + 1
	# this line ensures that "0" characters are not ommitted
	api_date_range = ("%02d" % depart_date.month) + ("%02d" % depart_date.day) + ("%02d" % return_date.month) + ("%02d" % return_date.day)

	gender_query = {}
	gender = user_voyages[0].gender
	gender_query[gender] = True

	# create a dict for the voyage type, find actual and set a value to True for that type
	voyage_query = {}
	voyage_type = user_voyages[0].voyage_type
	voyage_query[voyage_type] = True

	
	day_pretty = 1

	if depart_delta < 10 and return_delta < 10:
		use_ten_day_forecast = True
		api_call = API_URL_TEN_DAY % (WU_KEY, destination)
		api_data = requests.get(api_call).json()

		# TODO:		
		# else: add back error handling

		# get daily data from API call, used in daily forecast model
		forecast_alldays = {}
		for day in range(depart_delta, (return_delta+1)):
			forecast_alldays[day] = {'high_temp_f': int(api_data[u'forecast'][u'simpleforecast'][u'forecastday'][day][u'high'][u'fahrenheit']),
				'low_temp_f': int(api_data[u'forecast'][u'simpleforecast'][u'forecastday'][day][u'low'][u'fahrenheit']),
				'high_temp_c': int(api_data[u'forecast'][u'simpleforecast'][u'forecastday'][day][u'high'][u'celsius']),
				'low_temp_c': int(api_data[u'forecast'][u'simpleforecast'][u'forecastday'][day][u'low'][u'celsius']),
				'pop_percent': int(api_data[u'forecast'][u'simpleforecast'][u'forecastday'][day][u'pop']),
				'snow_in': int(api_data[u'forecast'][u'simpleforecast'][u'forecastday'][day][u'snow_allday'][u'in']), 
				'snow_cm': int(api_data[u'forecast'][u'simpleforecast'][u'forecastday'][day][u'snow_allday'][u'cm']), 
				'icon': (api_data[u'forecast'][u'simpleforecast'][u'forecastday'][day][u'icon_url']), 
				'day_pretty': day_pretty
				}
			day = day + 1
			day_pretty = day_pretty + 1
		
		# summarize the daily date for display on the main page
		forecast = {}
		for day in forecast_alldays:
			forecast['all_high_temp_f'] = forecast.get('all_high_temp_f', []) + [forecast_alldays[day]['high_temp_f']]
			forecast['high_temp_f'] = max(forecast['all_high_temp_f'])
			forecast['all_low_temp_f'] = forecast.get('all_low_temp_f', []) + [forecast_alldays[day]['low_temp_f']]
			forecast['low_temp_f'] = min(forecast['all_low_temp_f'])
			forecast['all_high_temp_c'] = forecast.get('all_high_temp_c', []) + [forecast_alldays[day]['high_temp_c']]
			forecast['high_temp_c'] = max(forecast['all_high_temp_c'])
			forecast['all_low_temp_c'] = forecast.get('all_low_temp_c', []) + [forecast_alldays[day]['low_temp_c']]
			forecast['low_temp_c'] = min(forecast['all_low_temp_c'])
			forecast['all_pop'] = forecast.get('all_pop', []) + [forecast_alldays[day]['pop_percent']]
			forecast['precip'] = max(forecast['all_pop'])
			forecast['all_snow'] = forecast.get('all_snow', []) + [forecast_alldays[day]['snow_in']]
			forecast['snow'] = max(forecast['all_snow'])
			forecast['icon'] = forecast.get('icon', []) + [forecast_alldays[day]['icon']]
			forecast['day_pretty'] = forecast.get('day_pretty', []) + [day_pretty]
			forecast['avg_temp_f'] = ((forecast['high_temp_f'] + forecast['low_temp_f'])/2)
			day_pretty = day_pretty + 1


	# this part of the code runs when the voyage takes place or ends more than 10 days in the future
	else: 
		use_ten_day_forecast = False
		api_call = API_URL_PLAN % (WU_KEY, api_date_range, destination)
		api_data = requests.get(api_call).json()
		forecast = {
				'max_temp_f': int(api_data[u'trip'][u'temp_high'][u'max'][u'F']),
				'max_temp_c': int(api_data[u'trip'][u'temp_high'][u'max'][u'C']),
				'avg_temp_f': int(api_data[u'trip'][u'temp_high'][u'avg'][u'F']),
				'avg_temp_c': int(api_data[u'trip'][u'temp_high'][u'avg'][u'C']),
				'min_temp_f': int(api_data[u'trip'][u'temp_low'][u'min'][u'F']),
				'min_temp_f': int(api_data[u'trip'][u'temp_low'][u'min'][u'C']),					
				'precip': int(api_data[u'trip'][u'chance_of'][u'chanceofrainday'][u'percentage']),
				'snow': int(api_data[u'trip'][u'chance_of'][u'chanceofsnowday'][u'percentage'])
				}
		# pass empty dict since this is not used for trips that are further out
		forecast_alldays = {}
		
	# calculate the temperature range using the average temp for the period
	temperature_query = {}
	if forecast['avg_temp_f'] >= 90:
		temperature_query['temp_high'] = True
	elif forecast['avg_temp_f'] < 90 and forecast['avg_temp_f'] >= 80:
		temperature_query['temp_medhigh'] = True
	elif forecast['avg_temp_f'] < 80 and forecast['avg_temp_f'] >= 60:
		temperature_query['temp_temp'] = True
	elif forecast['avg_temp_f'] < 60 and forecast['avg_temp_f'] >= 50:
		temperature_query['temp_medcold'] = True
	else:
		temperature_query['temp_cold'] = True

	# create a dict, valeez, to hold info shown in the view
	valeez = {}

	# query database
	valeez_garments = list(Garment.objects.filter(Q(**gender_query), Q(**voyage_query), Q(**temperature_query), Q(snow=False), Q(rain=False)))

	for item in valeez_garments:
		if item.layer == 0 or item.layer == 1:
			quantity = duration
		elif item.layer == 2 or item.layer == 3:
			if duration/2 < 1:
				quantity = 1
			else:
				quantity = int(duration/2)
		else:
			quantity = 1
		valeez[item.name] = quantity

	toiletries = Toiletry.objects.filter(Q(**gender_query), trip_duration__lte=duration)

	for item in toiletries:
		valeez[item.name] = 1

	# rain and snow items searched and added to another list if POP > 50%
	rain_snow_items = []
	if forecast['precip'] > 50:
		rain_items = list(Garment.objects.filter(rain=True))
		rain_snow_items = rain_snow_items + rain_items
	if forecast['snow'] > 50:
		snow_items = list(Garment.objects.filter(snow=True))
		rain_snow_items = rain_snow_items + snow_items

	for item in rain_snow_items:
		valeez[item.name] = 1

	item_count = sum(valeez.values())

	# save the valeez object
	vid = user_voyages[0].id
	valeez_object = Valeez(voyage_id=vid, contents=valeez)
	# check if vid is in db
	try:
		check_vid = Valeez.objects.get(voyage_id=vid)
	except ObjectDoesNotExist:
		check_vid = None
	
	if check_vid is None:
		valeez_object.save()
	else:
		return HttpResponseRedirect('/valeez_exists/', {})
	
	if 'error' in api_data:
		return render(request, 'valeezapp/error.html')

	return render(request,'valeezapp/show_valeez.html', {'user_today_date': user_today_date,'depart_delta': depart_delta, 'return_delta': return_delta, 'this_user':this_user, 'destination_pretty': destination_pretty, 'depart_date': depart_date, 'return_date': return_date, 'duration': duration, 'forecast': forecast, 'forecast_alldays': forecast_alldays, 'use_ten_day_forecast': use_ten_day_forecast, 'valeez': valeez, 'item_count': item_count})

def valeez_exists(request):
	return render(request, 'valeezapp/valeez_exists.html', {})

def sign_up(request):
	signed_up = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		user_profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and user_profile_form.is_valid():
			user = user_form.save()
			user.save()
			user_profile = user_profile_form.save(commit=False)
			user_profile.user = user
			user_profile.save()
			signed_up = True
	else:
		user_form = UserForm()
		user_profile_form = UserProfileForm()

	return HTTPResponseRedirect('registration/registration_form.html', {'user_form': user_form, 'user_profile_form': user_profile_form, 'signed_up': signed_up}, context)
	

def past_voyages(request):
	this_user = request.user
	voyages = Voyage.objects.filter(user=this_user).order_by('depart_date', 'destination')
	vquery=''
	if not voyages:
		any_voyages = False
		vquery=[]
	else: 
		any_voyages = True
		for voyage in voyages:
			voyage_query = Valeez.objects.filter(voyage=voyage.id)
		for item in voyage_query:
			vquery =item.__dict__
			vquery = ast.literal_eval(vquery['contents'])
	template = loader.get_template('valeezapp/past_voyages.html')
	context = RequestContext(request, {'voyages' : voyages, 'any_voyages': any_voyages, 'vquery': vquery})
	return HttpResponse(template.render(context))


def how_it_works(request):
	return render(request, 'valeezapp/how_it_works.html', {})


def about(request):
	return render(request, 'valeezapp/about.html', {})
