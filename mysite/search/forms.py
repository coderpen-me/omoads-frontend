from django import forms
from django.forms import ModelForm
from models import Owner

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

# class ContactForm(forms.Form):
# 	topic = forms.MultipleChoiceField(choices=TOPIC_CHOICES, widget=forms.CheckboxSelectMultiple)
# 	message = forms.CharField()
# 	sender = forms.EmailField(required=False)


class filterForm(forms.Form):
	type_banner = forms.MultipleChoiceField(choices=TYPE_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': '$("#filterForm").submit();'}))
	lighted_banner = forms.MultipleChoiceField(choices=LIGHTED_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': '$("#filterForm").submit();'}))
	max_cost_banner = forms.CharField( required=False, widget=forms.Select(attrs={'onchange': '$("#filterForm").submit();'}) )
	min_cost_banner = forms.CharField( required=False, widget=forms.Select(attrs={'onchange': '$("#filterForm").submit();'}) )
	dimensions_banner = forms.MultipleChoiceField(choices=DIMENSION_CHOICES, required=False, widget=forms.CheckboxSelectMultiple(attrs={'onchange': '$("#filterForm").submit();'}))

class signupForm(ModelForm):
	class Meta:
		model = Owner
		fields = ["company_name", "contact_number" , "email" , "password"]


	# company_name = forms.CharField( max_cost_banner = 100 )
	# contact_number = forms.CharField( max_cost_banner = 10 )
	# email = forms.EmailField( unique=True )
	# company_password = 
	# company_confirm_password = 