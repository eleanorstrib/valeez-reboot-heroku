from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView


urlpatterns =[
	url(r'^$', views.index, name='home'),
	url(r'^make_valeez/$', views.make_valeez, name='make_valeez'),
	url(r'^past_voyages/$', views.past_voyages, name='past_voyages'),
	url(r'^accounts/register/$', views.sign_up, name='sign_up'),
]