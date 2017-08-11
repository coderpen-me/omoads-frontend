from django import forms
from django.forms import ModelForm
# from models import Owner
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Agency
# from captcha.fields import CaptchaField

TOPIC_CHOICES = (
	('general', 'General enquiry'),
	('bug', 'Bug report'),
	('suggestion', 'Suggestion'),
)

TYPE_CHOICES = (
	('gantry', 'Gantry'),
	('unipole', 'Unipole'),
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
)


class filterForm(forms.Form):
	type_banner = forms.MultipleChoiceField(choices=TYPE_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': '$("#filterForm").submit();'}))
	lighted_banner = forms.MultipleChoiceField(choices=LIGHTED_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': '$("#filterForm").submit();'}))
	max_cost_banner = forms.CharField( required=False, widget=forms.Select(attrs={'onchange': '$("#filterForm").submit();'}) )
	min_cost_banner = forms.CharField( required=False, widget=forms.Select(attrs={'onchange': '$("#filterForm").submit();'}) )
	dimensions_banner = forms.MultipleChoiceField(choices=DIMENSION_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': '$("#filterForm").submit();'}))



class UserForm(forms.ModelForm):#user form pre build class
	username=forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username...'}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email...'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password...'}),min_length=6)
	class Meta:
		model = User
		fields = ['username', 'email', 'password1']

class AgencyForm(forms.ModelForm):
	agency_name=forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}))
	agency_state=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'email'}))
	agency_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'pwd'}),min_length=6)
	class Meta:
		model = Agency
		fields = ['agency_name', 'agency_state', 'agency_city']



class LoginForm(forms.Form):
	username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'pwd'}))
