from django.contrib import admin
from .models import Voyage, Garment, Toiletry, Valeez

allModels = [Voyage, Garment, Toiletry, Valeez]

admin.site.register(allModels)
