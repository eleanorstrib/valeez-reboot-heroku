from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Voyage
from functools import partial 
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
		


