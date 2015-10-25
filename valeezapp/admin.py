from django.contrib import admin
from .models import User, Voyage, Garment, Toiletry, Valeez

allModels = [User, Voyage, Garment, Toiletry, Valeez]

admin.site.register(allModels)
