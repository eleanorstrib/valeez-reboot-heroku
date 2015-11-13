
import os
import time
import requests

from django.shortcuts import render
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
	this_user = request.user
	user_voyages = Voyage.objects.filter(user=this_user).order_by('-id')
	destination = user_voyages[0].destination
	depart_date = user_voyages[0].depart_date
	return_date = user_voyages[0].return_date
	duration = return_date-depart_date
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

	return render(request, 'valeezapp/show_valeez.html', {'this_user':this_user, 'destination': destination, 'depart_date': depart_date, 'return_date': return_date, 'duration': duration, 'forecast': forecast})


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

