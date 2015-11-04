from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from valeezapp.models import Voyage
from .forms import VoyageForm


def index(request):
	return render(request, 'valeezapp/index.html', {})


def make_valeez(request):
	form = VoyageForm()
	if request.method == 'POST':
		form = VoyageForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request, 'valeezapp/make_valeez.html', {'form': form})


# def sign_up(request):
# 	form = SignUpUserForm()
# 	if request.method == 'POST':
# 		form = SignUpUserForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 	return render(request, 'valeezapp/sign_up.html', {'form': form})


def past_voyages(request):
	voyages = Voyage.objects.order_by('destination')
	template = loader.get_template('valeezapp/past_voyages.html')
	context = RequestContext(request, {'voyages' : voyages})
	return HttpResponse(template.render(context))