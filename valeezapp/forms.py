from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Voyage
from functools import partial 
import datetime as dt
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('mobile', 'gender')

class VoyageForm(forms.ModelForm):
	class Meta:
		widgets = {'depart_date': DateInput(), 'return_date': DateInput()}
		model = Voyage
		fields = ('destination', 'depart_date', 'return_date', 'voyage_type', 'gender')

	def clean(self):
		cleaned_dates = super(VoyageForm, self).clean()
		depart_date = cleaned_dates.get('depart_date')
		return_date = cleaned_dates.get('return_date')
		today = dt.date.today()

		if depart_date > return_date:
			raise forms.ValidationError('Oops - try again! Your return date must be after your departure date.')

		if depart_date < today:
			raise forms.ValidationError('Oops - try again! Your departure date must be in the future.')
		



