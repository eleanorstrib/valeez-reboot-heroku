from django.contrib import admin
from .models import User, Trip, Garment, Toiletry, Valeez

allModels = [User, Trip, Garment, Toiletry, Valeez]

admin.site.register(allModels)
