from django.contrib import admin
from .models import Voyage, Garment, Toiletry, Valeez, UserProfile

allModels = [UserProfile, Voyage, Garment, Toiletry, Valeez]

admin.site.register(allModels)
