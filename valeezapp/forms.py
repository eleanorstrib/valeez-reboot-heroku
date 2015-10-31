from django import forms
from .models import Voyage, User

class VoyageForm(forms.ModelForm):
	class Meta:
		model = Voyage
		fields = ('destination', 'depart_date', 'return_date', 'voyage_type',)


class SignUpUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'gender', 'email', 'mobile', 'home_timezone')