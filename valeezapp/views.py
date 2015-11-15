
import os
import time
import requests

from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from valeezapp.models import UserProfile, Voyage, Valeez, Garment, Toiletry
from django.template.defaultfilters import slugify
from .forms import UserForm, UserProfileForm, VoyageForm

WU_KEY = os.environ.get('WU_API_KEY')
API_URL = "http://api.wunderground.com/api/%s/planner_%s/q/%s.json"


def index(request):
	return render(request, 'valeezapp/index.html', {})


def make_valeez(request):
	form = VoyageForm()
	if request.method == 'POST':
		form = VoyageForm(request.POST)
		if form.is_valid():
			# form.save()
			link_user = form.save(commit=False)
			link_user.user = request.user
			link_user.save()
	return render(request, 'valeezapp/make_valeez.html', {'form': form})


def show_valeez(request):
	# user data for the view and to construct the API call
	this_user = request.user
	user_voyages = Voyage.objects.filter(user=this_user).order_by('-id')
	destination = user_voyages[0].destination
	destination_pretty = str(destination)[3:]
	depart_date = user_voyages[0].depart_date
	return_date = user_voyages[0].return_date
	duration = str(return_date-depart_date)[:2]
	duration_int = int(duration)
	
	voyage_type = user_voyages[0].voyage_type


	# put together variables for the API call 
	api_date_range = str(depart_date.month) + str(depart_date.day) + str(return_date.month) + str(return_date.day)
	api_call = API_URL % (WU_KEY, api_date_range, destination)
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

	# categorize forecast variables
	if forecast['avg_temp_f'] >= 90:
		temp_cat = 'temp_high'
	elif forecast['avg_temp_f'] < 90 and forecast['avg_temp_f'] >= 80:
		temp_cat = 'temp_medhigh'
	elif forecast['avg_temp_f'] < 80 and forecast['avg_temp_f'] >= 60:
		temp_cat = 'temp_temp'
	elif forecast['avg_temp_f'] < 60 and forecast['avg_temp_f'] >= 50:
		temp_cat = 'temp_medcold'
	else:
		temp_cat = 'temp_cold'

	valeez = {}
	# all_temps = Q(garment__contains='temp_all')
	# forecast_temp=Q(garment__contains=temp_cat)

	if user_voyages[0].gender == "female":
		valeez_garments = list(Garment.objects.filter(temp='temp_all', female=True))
		valeez_temp_spec = list(Garment.objects.filter(temp=temp_cat, female=True))
		valeez_garments = valeez_garments + valeez_temp_spec
	else:
		valeez_garments= list(Garment.objects.filter(temp='temp_all', male=True))
		valeez_temp_spec = list(Garment.objects.filter(temp=temp_cat, male=True))
		valeez_garments = valeez_garments + valeez_temp_spec
	
	
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

	return render(request, 'valeezapp/show_valeez.html', {'this_user':this_user, 'destination_pretty': destination_pretty, 'depart_date': depart_date, 'return_date': return_date, 'duration': duration, 'forecast': forecast, 'valeez': valeez})


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

	return render(request, 'registration/registration_form.html', {'user_form': user_form, 'user_profile_form': user_profile_form, 'signed_up': signed_up})


# This view feeds into past_voyages.html
def past_voyages(request):
	this_user = request.user
	voyages = Voyage.objects.filter(user=this_user).order_by('depart_date', 'destination')
	template = loader.get_template('valeezapp/past_voyages.html')
	context = RequestContext(request, {'voyages' : voyages})
	return HttpResponse(template.render(context))

