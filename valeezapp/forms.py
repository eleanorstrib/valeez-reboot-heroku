from django import forms
from registration.forms import RegistrationForm
from registration.models import RegistrationProfile
from django.contrib.auth.models import User
from .models import Voyage
from functools import partial 
import datetime as dt
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    # def clean(self):
    # 	cleaned_userform = super(UserProfileForm, self).clean()
    # 	password = cleaned_userform.get('password')

    # 	if len(password) < 8 or len(password) > 20:
    # 		raise.forms.ValidationError('Password must be 8-20 characters long.')

class VoyageForm(forms.ModelForm):
	class Meta:
		widgets = {'depart_date': DateInput(), 'return_date': DateInput()}
		model = Voyage
		fields = ('destination', 'depart_date', 'return_date', 'voyage_type', 'gender')
		error_css_class = 'error'

	def clean(self):
		cleaned_dates = super(VoyageForm, self).clean()
		destination = cleaned_dates.get('destination')
		depart_date = cleaned_dates.get('depart_date')
		return_date = cleaned_dates.get('return_date')
		trip_type = cleaned_dates.get('trip_type')
		gender = cleaned_dates.get('gender')
		today = dt.date.today()

		# all conditions for validation
		if destination == None or depart_date == None or return_date == None:
			raise forms.ValidationError('All fields are required!')

		if depart_date > return_date:
			raise forms.ValidationError('Your return date must be after your departure date.')

		if depart_date < today:
			raise forms.ValidationError('Your departure date must be in the future.')
		



