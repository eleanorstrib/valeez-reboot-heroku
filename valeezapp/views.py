from django.shortcuts import render
from valeezapp.models import User, Voyage, Garment, Toiletry, Valeez

def index(request):
	return render(request, 'valeezapp/index.html', {})

def past_voyages(request):
	voyages = Voyage.objects.all()
	return render(request, 'valeezapp/past_voyages.html', {'voyages' : voyages,
		})