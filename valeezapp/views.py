from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from valeezapp.models import Voyage
from .forms import UserForm, UserProfileForm, VoyageForm


def index(request):
	return render(request, 'valeezapp/index.html', {})


def make_valeez(request):
	form = VoyageForm()
	if request.method == 'POST':
		form = VoyageForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'valeezapp/make_valeez.html', {'form': form})


def sign_up(request):
	form = UserForm()
	# user_profile_form = UserProfileForm()

	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
	# 	user_profile_form = UserProfileForm(request.POST)
	# 	if user_form.is_valid() and user_profile_form.is_valid():
	# 		user = user_form.save()
	# 		user.save()
	# 		user_profile = user_profile_form.save(commit=False)
	# 		user_profile.user = user
	# 		user_profile.save()
	# 		signed_up = True
	# else:
	# 	user_form = UserForm()
	# 	user_profile_form = UserProfileForm()

	return render(request, 'registration_form.html', {'form': form})


def past_voyages(request):
	voyages = Voyage.objects.order_by('destination')
	template = loader.get_template('valeezapp/past_voyages.html')
	context = RequestContext(request, {'voyages' : voyages})
	return HttpResponse(template.render(context))