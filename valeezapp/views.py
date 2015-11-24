
import os
import time
import requests

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse 
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from valeezapp.models import UserProfile, Voyage, Valeez, Garment, Toiletry
from django.template.defaultfilters import slugify
from .forms import UserForm, UserProfileForm, VoyageForm
from django.db.models import Q

WU_KEY = os.environ.get('WU_API_KEY')
API_URL = "http://api.wunderground.com/api/%s/planner_%s/q/%s.json"


def index(request):
	user = request.user
	return render(request, 'valeezapp/index.html', {'user': user})


def make_valeez(request):
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
	This view runs the API call for the forecast and assembles a valeez for a new voyage.
	"""
	this_user = request.user
	
	# retrieving data about the last voyage created
	user_voyages = Voyage.objects.filter(user=this_user).order_by('-id')
	
	destination = user_voyages[0].destination
	destination_pretty = (str(destination)[3:]).replace('_', ' ')
	depart_date = user_voyages[0].depart_date
	return_date = user_voyages[0].return_date

	# create a dict for the voyage type
	voyage_query = {}
	#find actual voyage type
	voyage_type = user_voyages[0].voyage_type
	#set that value in dict to True
	voyage_query[voyage_type] = True

	#TODO: use the datetime delta attributes to get duration number
	duration = str(return_date-depart_date)[:2]
	duration_int = int(duration)

	# put together variables for the API call
	api_date_range = str(depart_date.month) + str(depart_date.day) + str(return_date.month) + str(return_date.day)
	api_call = API_URL % (WU_KEY, api_date_range, destination)
	api_data = requests.get(api_call).json()

	# add error handling - any issues adds a key called 'error' to response
	if 'error' in api_data:
		return render(request, 'valeezapp/error.html')
	else: 
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

	# categorize forecast variables into temp categories, add  appropriate value to dict
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
	if user_voyages[0].gender == "female":
		valeez_garments = list(Garment.objects.filter(Q(female=True), Q(**voyage_query), Q(**temperature_query), Q(snow=False), Q(rain=False)))
	else:
		valeez_garments = list(Garment.objects.filter(Q(male=True), Q(**voyage_query), Q(**temperature_query), Q(snow=False), Q(rain=False)))

	for item in valeez_garments:
		if item.layer == 0 or item.layer == 1:
			quantity = duration_int
		elif item.layer == 2 or item.layer == 3:
			if duration_int/2 < 1:
				quantity = 1
			else:
				quantity = int(duration_int/2)
		else:
			quantity = 1
		valeez[item.name] = quantity

	toiletries = Toiletry.objects.filter(trip_duration__lte=duration_int)

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
	valeez_object.save()

	return render(request,'valeezapp/show_valeez.html', {'voyage_id': vid, 'this_user':this_user, 'destination_pretty': destination_pretty, 'depart_date': depart_date, 'return_date': return_date, 'duration': duration, 'item_count': item_count,'forecast': forecast, 'valeez': valeez})


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
	

# This view feeds into past_voyages.html
def past_voyages(request):
	this_user = request.user
	voyages = Voyage.objects.filter(user=this_user).order_by('depart_date', 'destination')
	for voyage in voyages:
		voyage.query = Valeez.objects.filter(voyage=voyage.id)
	template = loader.get_template('valeezapp/past_voyages.html')
	context = RequestContext(request, {'voyages' : voyages})
	return HttpResponse(template.render(context))

