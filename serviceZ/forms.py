from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, ServiceType, Service

#SERVICETYPE_CHOICES = tuple(Service.objects.all().values_list())



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
	#zipcode = forms.IntegerField(required=True, max_value=99999, # not working
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
		model = Account
		fields = [
		'username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'check',
		]

class UpdateAccountForm(forms.Form):
	Zipcode = forms.IntegerField(label="zipcode", max_value=99999, min_value=0)
	Language = forms.CharField(label="language", max_length=200)

class AddServiceForm(forms.Form):
	ServiceType = forms.CharField(label="Service Type", max_length=200)

class BecomeClientForm(forms.Form):
	clientButton = forms.BooleanField(label="Client Button")


class BecomeContractorForm(forms.Form):
	Job_Menu = forms.ModelChoiceField(queryset=Service.objects.all().values_list('Description', flat=True),
									  label="Type Of Work Intrested In", to_field_name='Description')

class SearchBarForm(forms.Form):
	searchBar = forms.CharField(label="", max_length=200)