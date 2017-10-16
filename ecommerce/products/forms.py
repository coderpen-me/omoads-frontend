from django import forms
from django.forms import ModelForm
# from models import Owner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Agency, Zone
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
	type_banner = forms.MultipleChoiceField(choices=TYPE_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': '$("#filterForm").submit();'}))
	lighted_banner = forms.MultipleChoiceField(choices=LIGHTED_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': '$("#filterForm").submit();'}))
	max_cost_banner = forms.CharField( required=False, widget=forms.Select(attrs={'onchange': '$("#filterForm").submit();'}) )
	min_cost_banner = forms.CharField( required=False, widget=forms.Select(attrs={'onchange': '$("#filterForm").submit();'}) )
	dimensions_banner = forms.MultipleChoiceField(choices=DIMENSION_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': '$("#filterForm").submit();'}))



class UserForm(forms.ModelForm):#user form pre build class
	username=forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username...','onkeyup':'checkUserName(this)'}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email...','onkeyup':'checkEmail(this)'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password...','onkeyup':'password(this)'}),min_length=6)
	class Meta:
		model = User
		fields = ['username', 'email', 'password1']

class AgencyForm(forms.ModelForm):

	agency_name=forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter agency_name...', 'id': 'name','onkeyup':'agencyName(this)'}))
	agency_state=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter agency_state...', 'id': 'state','onkeyup':'stateName(this)'}))
	agency_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter agency_city...', 'id': 'city','onkeyup':'cityName(this)'}),min_length=6)


	class Meta:
		model = Agency
		fields = ['agency_name', 'agency_state', 'agency_city']



class LoginForm(forms.Form):
	username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username...', 'id': 'email','onkeyup':'checkUserNameLogin(this)'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password...', 'id': 'pwd'}))
