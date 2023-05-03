from django import forms
#from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model

#User = get_user_model()

from django.contrib.auth.forms import UserCreationForm
from .models import Account
#from django.contrib.auth.models import UserManager
from django.conf import settings


# Create your forms here.

class RegisterForm(UserCreationForm):
	email = forms.EmailField(
	max_length=100,
	required = True,
	help_text='Enter Email Address',
	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
	)
	first_name = forms.CharField(
	max_length=100,
	required = True,
	help_text='Enter First Name',
	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
	)
	last_name = forms.CharField(
	max_length=100,
	required = True,
	help_text='Enter Last Name',
	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
	)
	username = forms.CharField(
	max_length=200,
	required = True,
	help_text='Enter Username',
	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
	)
	#zipcode = forms.IntegerField(required=True, max_value=99999,
	#							 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zipcode'}))
	password1 = forms.CharField(
	help_text='Enter Password',
	required = True,
	widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
	)
	password2 = forms.CharField(
	required = True,
	help_text='Enter Password Again',
	widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
	)
	check = forms.BooleanField(required = True)

	class Meta:
		#objects = User #UserManager()
		model = Account #settings.AUTH_USER_MODEL done
		fields = [
		'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'check',
		]

