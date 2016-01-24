from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView


urlpatterns =[
	
	url(r'^$', views.index, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^how_it_works/$', views.how_it_works, name='how_it_works'),
	url(r'^make_demo_valeez/$', views.make_demo_valeez, name='make_demo_valeez'),
	url(r'^show_demo_valeez/$', views.show_demo_valeez, name='show_demo_valeez'),
	url(r'^make_valeez/$', views.make_valeez, name='make_valeez'),
	url(r'^show_valeez/$', views.show_valeez, name='show_valeez'),
	url(r'^past_voyages/$', views.past_voyages, name='past_voyages'),
	url(r'^valeez_exists/$', views.valeez_exists, name='valeez_exists'),
]