from myapp.models import Credentials
from django.forms import ModelForm
from django import forms


class RegForm(ModelForm):
	class Meta:
		model=Credentials
		fields=['passw','usern']

class login_form(forms.Form):
	#your_name = forms.CharField(label='Your name', max_length=100)
	user_name = forms.CharField(max_length=30)
	pass_word = forms.CharField(max_length=20)
	