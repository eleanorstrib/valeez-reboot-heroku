from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns =[
	url(r'^$', views.index, name='home'),
	url(r'^past_voyages/$', views.past_voyages, name='past_voyages'),
]