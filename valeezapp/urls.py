from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns =[
	url(r'^$', views.index, name='home'),
	url(r'^past_voyages/$', TemplateView.as_view(template_name='past_voyages.html'),
	 name='past_voyages'),
]