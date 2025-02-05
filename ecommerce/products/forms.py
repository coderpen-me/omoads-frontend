from django import forms
from django.forms import ModelForm
# from models import Owner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.admin.helpers import ActionForm
from django.forms import extras

# from captcha.fields import CaptchaField

TOPIC_CHOICES = (
	('general', 'General enquiry'),
	('bug', 'Bug report'),
	('suggestion', 'Suggestion'),
)

TYPE_CHOICES = (
	('gantry', 'Gantry'),
	('unipole', 'Unipole'),
	('traffic_light', 'Traffic Light Signage'),
)

LIGHTED_CHOICES = (
	('f', 'Front Lit'),
	('b', 'Back Lit'),
	('n', 'Not Lighted'),
)

DIMENSION_CHOICES = (
	('0', '50x10'),
	('1', '40x10'),
	('2', '30x10'),
	('3', '20x10'),
	('4', '8x4'),
)


class filterForm(forms.Form):
	type_banner = forms.MultipleChoiceField(choices=TYPE_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': 'submit_filter();'}))
	lighted_banner = forms.MultipleChoiceField(choices=LIGHTED_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': 'submit_filter();'}))
	max_cost_banner = forms.CharField( required=False, widget=forms.Select(attrs={'onchange': 'submit_filter();'}) )
	min_cost_banner = forms.CharField( required=False, widget=forms.Select(attrs={'onchange': 'submit_filter();'}) )
	dimensions_banner = forms.MultipleChoiceField(choices=DIMENSION_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': 'submit_filter();'}))



class UserForm(forms.ModelForm):#user form pre build class
	first_name=forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first Name...',"style":"border:2px solid #d2bd7f;border-radius:0px;background:#cacaca;"}))
	last_name=forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last Name...', "style":"border:2px solid #d2bd7f;border-radius:0px;background:#cacaca;"}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', "style":"border:2px solid #d2bd7f;border-radius:0px;background:#cacaca;"}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', "style":"border:2px solid #d2bd7f;border-radius:0px;background:#cacaca;"}),min_length=6)
	class Meta:
		model = User
		fields = [ 'first_name', 'last_name', 'email', 'password1']

class AgencyForm(forms.ModelForm):

	agency_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter agency_name...', 'id': 'name','onkeyup':'agencyName(this)'}))
	agency_state=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter agency_state...', 'id': 'state','onkeyup':'stateName(this)'}))
	agency_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter agency_city...', 'id': 'city','onkeyup':'cityName(this)'}),min_length=6)


	class Meta:
		model = Agency
		fields = ['agency_name', 'agency_state', 'agency_city']



class LoginForm(forms.Form):
	username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username...', 'id': 'email','onkeyup':'checkUserNameLogin(this)'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password...', 'id': 'pwd'}))


class UpdateActionForm(ActionForm):
    price = forms.FloatField()
    startDate = forms.DateField(widget = extras.SelectDateWidget)
    endDate = forms.DateField(widget = extras.SelectDateWidget)